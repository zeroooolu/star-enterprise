module.exports = async function handler(req, res) {
  const presetId = '2097207849833730048';
  const base = 'https://gw.kanjian.com/contract/api/v1';

  const exportTargets = {
    '番茄音乐': { name: '番茄畅听' },
    '咪咕音乐': { id: '5' },
    '阿里音乐': { id: '7' },
    'Deezer': { id: '11' },
    'Meta（Facebook / Instagram）': { id: '430' },
    'Qobuz': { id: '380' },
    'SoundCloud': { id: '98' },
    'TIDAL': { id: '21' },
    'Yandex': { id: '59215' }
  };

  // User-confirmed / official static brand assets that are not present in the Star preset.
  // Bandcamp is the exact icon supplied for this prototype. Beatport uses Beatport's official
  // downloadable black wordmark asset from its support site.
  const staticLogos = {
    'Bandcamp': 'data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAFAAAABQCAYAAACOEfKtAAAAAXNSR0IArs4c6QAAAERlWElmTU0AKgAAAAgAAYdpAAQAAAABAAAAGgAAAAAAA6ABAAMAAAABAAEAAKACAAQAAAABAAAAUKADAAQAAAABAAAAUAAAAAAx4ExPAAAIcElEQVR4Ae2da2wUVRTHb2e3j223pS1Lty0F2gqlah9pwSZAIYHEqKlRUYJNiYCxFUxADSZ+UEwIH0yMkRANRmyraEKDSKKJNlE+0Ig0BAMlLRUpRShtoQ+2tND37nbX81+6a7vsa2ZnZofu3KSZ7cy9d+79zbn3nnNm5kwEE5a0OTk5xvLy8hy73V5YXFy8LC8vbzHHcWkajcYQERGhp98xtI2i6jX0xwk7TdClbFTDFLXRbLPZJmg7MjU1ZaLfPa2trZ1NTU3t1MbmY8eOXaXUR3mtfM8YwafAqlWrkisrKzcWFRVtSklJKYqJiTFGRkYygsaoIXyqCnlegskIJrNYLGxiYqKvv7//IqUTNTU1P509e/ZuoA0MqNdr1qyJr6qqeru0tHSHwWBYqNVquUcNmD8gAGq1Wm0mk+nWmTNnDldXV3/e2Ng47K+cP4Dcnj17nt2+ffvHS5YsKSRw/uqbE8cJJLt582bzkSNHPjhw4MBv1ClMBR6TL4Ca+vr6fStXrnwvLi5ON9ckziONGTshkaOjo+Pnz5//rKysbB8dmppx2PXT4+SemZmZePr06e9Wr179oV6vDzt4oAOBQd/BACzAxEVtxg9PEqhBgYKCgi1YINTEHAtNS0vL0XXr1m0jHrMk0V0COQzb/Pz8ChXe/6IDFmACNrR3FjPoaK5EC8ZzmzdvPqjT6VTRc1F58INUtQjSQJ4iHbKJ1Jx252EXQKgqe/fuPWo0GjPCbcFwwvC3JUmMJG0kD8O5q6vLjPwucYSeB1VFhecdI9iAEVg5czkAwsKAkhwuep6z80K2YARWYIbyDoAwz2BhCKkwHMuAFZg5AWph28I8C0cYQvoMVmBGZbUcvCpwDKhzX+AowQrMwI6rqKhYTmqLMfDiak4QgCcK7jyOXDoF6uLBXyigXJO9XMjBGQp/npr4EQAzsOPgSVbnP37wkBvMpr3wXBr/4moJEMAtDI5E0aDiEEYA7AgipxdWXC1Fw1iPexs6FYUwAiR8Oi0BDInrypMnV1g3xCllF1AN2OEukew6jI3uN3x0oZMNTfK+DSugm/6LAN7TCxPZxsz5/jPPzqEBQFltYEjer52D7MfrA4xTiBgmRWvZ+4UZs9EE9h8nKzy06Z5lilW39SkGHg0GtilrPsvSRweGzC2XrAAhcCduDLD2e+NuzQjdv5C+N5YbmZA5EK2WFaBpwsq+b+8PHS23MwPazsdTWVKU8AcGZANIlg/7/lo/6xlz3Epw60po/s2Kj2YvZSYLlj60WjaAXSNmVnftDlPIukG2LKQvLSjpkw0gJuqvr/SyYVpAlJJy5+lY2aKkoKRPNoBXhsbYL50BPzEmOWOMgnfy0lmkCHqU5EMYjf3icg8bs3p9wElyYDNPgIWjNDWBraU/MZKkAAHvgmmUNdy+p5i5L0bDscpcI9NgEhQhSQpw0mZnB1tvBT3PiNBPRxWQvmcyElnJgnixqpRuFcb1PXV7yCGBorU2yIqiaM57i1ZecWTvQWMkk8CxKRs7/E8vnvAOstviFEczXn3MwLIThJls3lohCUBc4Z877rLLQ8ox2Qz0wNnrOWSyiXw9JQEIfa+2rVfUoeJNAgLdX55tYAtj8daFuEkSgN9c7Wfdo8ox2TLiokj6UsQlN12b6ABvEbgfrt+RpLFCKsWIrVyeyuIjpfEbiwoQqtW39MKPaVwZnmYAfyJRx14M0mHg68KJCvD6/QmSPpPDUPd1UrmOQVneQe6qWFKepUqi1Yyh8iWpLWZSnpWSVhj0bEN6oqSKvGgA/+ofZr93Dylm5cV08i45DKJFcBj4EghRAEJZxn2OSVKelZAwBjakJbIVhjhJpQ99FQXgn733WWPffcVIXyw9bLvryVTJ4YkC0OJwGNwWXcNH44SmFxYns9x5sUKL8yoXlATCZKvvusvaFHSXDfrem7mpsmkCQQEcNFvZV5d7FSN9mPu2LF3AYHnIlQQDdDoMboxMytVWv+dJI4fBa0tTZJn7nI0RDNAhfaT3AaRS0jaydw0xwu/xCumHIICAVnOljw0q5OEgdHwZ3WV7Jcsgq/ThvIIA3hieZCc6BmSbqNFQXwnGTxU9njFPIoeBr3ND3qH98gJ5cWCEFc+PU8zwTaTnW55fHPw9Xl+gvByzRXR3d5uTkpJ4P2SppLkPnQuFBT44OGjR0ssiFjo/b4ChaLAXKQjZbmJn5ugNbOXcuAgZCmEnRjQkjiiOCCuulgI7vCtnUlEIIwB2GMI9woqrpcCOQxQzEkWVBk8CYAZ2HELAIYqZmvgRADOww5tKzQgBpyZ+BMAM7DgEH0T8PH7F1dxgBnYcIjci+KA6DwYuFGAFZmAHG9iKyI0IPhh4FeGdE6zADOwcTgSEvUTkxvDGEnjvwQrMUMIBEDFDEfYSkRvV5JsAGIGVM86qy42FmKEIe6nOhd4Bgg0YgZUzl+uRJUQjo/gxnSUlJS9HRUXx9s44K5zLW4QEPXTo0I7jx4//7eynCyB2kFj+u379+uj09PS1FA9AaS4/Z5tDsjWbzfZz5859snv37hpqgMt08wRJDQHqdomgNHsLATpLAqfL2RsaGk5R8NVFFKUsP9wlEZJ36dKluq1bt+4aGnr4oW9PEujkr6EhvS87O1sNg+wjDLInCXQCtNfW1v5BLpsmhL1MSEhIpSgVzmNzegtVpaOjoxkLxvSc59XI8AUQkOwkhe0Y/7GxsaPJycnLKGpZPIEkO9qX8D56fKGiwMIgE6375MmTn+7fv3/n9GrrWjA89YoXBfePESBsHiK/0TwJz4Sn+hW7D8DgkoK0jY+PS/sxAg8UHJ/DQOxBakSB++cwEA2JgCICOvRJSHmoxj6GHj6HYaGpaJy2D30Ogy5+S11dXZvQz2H8BzCCLa6QjOlwAAAAAElFTkSuQmCC',
    'Beatport': 'https://support.beatport.com/hc/en-us/article_attachments/20473955236756'
  };

  try {
    const commonHeaders = { accept: 'application/json', tenantKey: 'star' };
    const labelResp = await fetch(`${base}/preset/sharing/${presetId}/preset-label`, { headers: commonHeaders });
    if (!labelResp.ok) throw new Error(`preset-label ${labelResp.status}`);
    const label = await labelResp.json();
    const labelData = label && label.data !== undefined ? label.data : label;
    const body = { dspName: '', areaIds: [], presetId, tId: labelData && labelData.allDsp ? '1' : '2', language: 'ZH_CN' };

    const dspResp = await fetch(`${base}/preset/sharing/allOrPersonalization/dsps-info`, {
      method: 'POST',
      headers: { ...commonHeaders, 'content-type': 'application/json' },
      body: JSON.stringify(body)
    });
    if (!dspResp.ok) throw new Error(`dsps-info ${dspResp.status}`);
    const dsp = await dspResp.json();
    const root = dsp && dsp.data !== undefined ? dsp.data : dsp;
    const groups = [...(root.includeList || []), ...(root.excludeList || [])];
    const items = groups.flatMap(group => group.dspList || []);

    const logos = { ...staticLogos };
    await Promise.all(Object.entries(exportTargets).map(async ([key, target]) => {
      const item = items.find(x => target.id ? String(x.dspId) === target.id : x.name === target.name);
      if (!item || !item.logoPath) return;
      const imageResp = await fetch(item.logoPath);
      if (!imageResp.ok) return;
      const mime = imageResp.headers.get('content-type') || 'application/octet-stream';
      const buf = Buffer.from(await imageResp.arrayBuffer());
      logos[key] = `data:${mime};base64,${buf.toString('base64')}`;
    }));

    res.setHeader('content-type', 'application/javascript; charset=utf-8');
    res.setHeader('cache-control', 'public, s-maxage=86400, stale-while-revalidate=604800');
    res.status(200).send(`window.STAR_DSP_LOGOS=${JSON.stringify(logos)};\n`);
  } catch (error) {
    res.setHeader('content-type', 'application/javascript; charset=utf-8');
    res.setHeader('cache-control', 'no-store');
    res.status(200).send(`window.STAR_DSP_LOGOS=${JSON.stringify(staticLogos)};\n`);
  }
};
