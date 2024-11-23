'use strict';

// 最大文字数を超えた場合の省略処理
export function truncateText(selector, MaxLength, imgSelector = null) {
  const elm = document.querySelector(selector);
  let targetText = elm.textContent.trim();
  const img = elm.querySelector(imgSelector);
  
  if (targetText.length > MaxLength) {
    const shortText = targetText.substring(0, MaxLength) + "...";
    elm.innerHTML = '';
    
    if (img) {
      elm.appendChild(img);
    }
    
    const textNode = document.createTextNode(shortText);
    elm.appendChild(textNode);
  }
}
