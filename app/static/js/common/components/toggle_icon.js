'use strict';

export function toggleIconState(imgSelector) {
  const icons = document.querySelectorAll(imgSelector);
  
  icons.forEach(function(icon) {
    icon.addEventListener("click", function() {
      const id = icon.getAttribute("data-id");
      const currentSrc = icon.getAttribute("src");
      const defaultSrc = `/static/images/${id}.svg`;
      const activeSrc = `/static/images/${id}_active.svg`;

      if (currentSrc === defaultSrc) {
        icon.setAttribute("src", activeSrc);
      } else {
        icon.setAttribute("src", defaultSrc);
      }
    });
  });
}
