document.querySelectorAll('article img').forEach($e => {
  $e.title = $e.alt; // add title to each image, based on the alt desc
});
