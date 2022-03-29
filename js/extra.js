// add title to each image, based on the alt desc
document.querySelectorAll('article img').forEach($e => {
  $e.title = $e.alt;
});

// add an anchor to each title
let title_id = 1;
document.querySelectorAll('article h2').forEach($e => {
  let $link = document.createElement('a');
  let _id = `title-${title_id}`;
  $link.innerText = '#';
  $link.href= '#' + _id;
  $link.classList.add('anchor')
  $e.id = _id;

  $e.appendChild($link);
  title_id += 1;
});
