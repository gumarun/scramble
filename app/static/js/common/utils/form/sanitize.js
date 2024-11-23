'use strict';

// input の入力値のパターンを制御
export function removeSpaces() {
  const inputs = document.querySelectorAll('input, textarea');
  
  inputs.forEach(input =>{
    input.addEventListener('input', () => {
      // 入力値からスペースを削除
      input.value = input.value.replace(/\s+/g, '');
    });
  });
}
