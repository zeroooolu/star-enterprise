import { readFile, readdir } from "node:fs/promises";
import { extname, join, relative } from "node:path";
import { fileURLToPath } from "node:url";

const ROOT = fileURLToPath(new URL("../", import.meta.url));
const UI_DIRECTORIES = ["prototype-v4", "enterprise-admin"];
const UI_EXTENSIONS = new Set([".css", ".html", ".js"]);
const BRAND_HEX = "#0040ff";

function hslFromRgb(red, green, blue) {
  const [r, g, b] = [red, green, blue].map((value) => value / 255);
  const max = Math.max(r, g, b);
  const min = Math.min(r, g, b);
  const lightness = (max + min) / 2;

  if (max === min) return { hue: 0, saturation: 0, lightness };

  const delta = max - min;
  const saturation = lightness > 0.5
    ? delta / (2 - max - min)
    : delta / (max + min);
  let hue;

  if (max === r) hue = (g - b) / delta + (g < b ? 6 : 0);
  else if (max === g) hue = (b - r) / delta + 2;
  else hue = (r - g) / delta + 4;

  return { hue: hue * 60, saturation, lightness };
}

function isUnapprovedBlue(red, green, blue) {
  if (red === 0 && green === 64 && blue === 255) return false;

  const { hue, saturation, lightness } = hslFromRgb(red, green, blue);
  const isBlueHue = hue >= 195 && hue <= 250;
  // Cool grays such as #eef2f7 remain neutral; only visibly chromatic blues fail.
  const isChromatic = saturation >= 0.45;
  const isVisibleAccent = lightness >= 0.22;
  const isDarkNeutral = lightness < 0.32 && saturation < 0.65;

  return isBlueHue && isChromatic && isVisibleAccent && !isDarkNeutral;
}

function parseHex(value) {
  const raw = value.slice(1);
  const expanded = raw.length === 3
    ? raw.split("").map((part) => part + part).join("")
    : raw;
  return [0, 2, 4].map((index) => Number.parseInt(expanded.slice(index, index + 2), 16));
}

function lineNumber(source, index) {
  return source.slice(0, index).split("\n").length;
}

async function collectFiles(directory) {
  const entries = await readdir(directory, { withFileTypes: true });
  const files = [];

  for (const entry of entries) {
    const path = join(directory, entry.name);
    if (entry.isDirectory()) files.push(...await collectFiles(path));
    else if (UI_EXTENSIONS.has(extname(entry.name))) files.push(path);
  }

  return files;
}

const violations = [];

for (const directory of UI_DIRECTORIES) {
  const absoluteDirectory = join(ROOT, directory);
  for (const file of await collectFiles(absoluteDirectory)) {
    const source = await readFile(file, "utf8");
    const colors = [
      ...source.matchAll(/#[0-9a-f]{6}|#[0-9a-f]{3}(?![0-9a-f])/gi),
      ...source.matchAll(/rgba?\(\s*(\d{1,3})\s*,\s*(\d{1,3})\s*,\s*(\d{1,3})(?:\s*,[^)]*)?\)/gi),
    ];

    for (const match of colors) {
      const value = match[0].toLowerCase();
      if (value === BRAND_HEX) continue;

      const rgb = value.startsWith("#")
        ? parseHex(value)
        : match.slice(1, 4).map(Number);
      if (!isUnapprovedBlue(...rgb)) continue;

      violations.push({
        file: relative(ROOT, file),
        line: lineNumber(source, match.index),
        value: match[0],
      });
    }
  }
}

if (violations.length) {
  console.error("Unapproved blue colors found. Use var(--brand-blue) or rgba(var(--brand-blue-rgb), alpha):");
  for (const violation of violations) {
    console.error(`  ${violation.file}:${violation.line} ${violation.value}`);
  }
  process.exitCode = 1;
} else {
  console.log("Brand color check passed: no unapproved blue accents found.");
}
