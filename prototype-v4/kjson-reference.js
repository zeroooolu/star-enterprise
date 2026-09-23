(async function loadKjsonReference(){
  const target=document.getElementById('guide-kjson');
  if(!target)return;

  if(!document.querySelector('link[data-kjson-reference]')){
    const link=document.createElement('link');
    link.rel='stylesheet';
    link.href='/prototype-v4/kjson-reference.css';
    link.dataset.kjsonReference='1';
    document.head.appendChild(link);
  }

  try{
    const response=await fetch('/prototype-v4/kjson-reference.html',{cache:'no-cache'});
    if(!response.ok)throw new Error('K-JSON reference load failed');
    const html=await response.text();
    target.outerHTML=html;
    if(location.hash&&location.hash.startsWith('#kjson-')){
      requestAnimationFrame(()=>document.querySelector(location.hash)?.scrollIntoView());
    }
  }catch(error){
    console.warn(error);
  }
})();
