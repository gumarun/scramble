'use strict';

// 文字数の制御
export function handleCharCount() {
  const inputWraps = document.querySelectorAll('.form-input-wrap');
  
  inputWraps.forEach(wrap => {
    const inputs = wrap.querySelectorAll('input, textarea');
    const charCount = wrap.querySelector('.char-count');
    const currentLength = wrap.querySelector('.current-length');
    const maxLength = wrap.querySelector('.max-length').textContent;
    
    inputs.forEach(input =>{
      // すでに入力されている文字数が最大文字数の場合
      const count = input.value.length;
      if (count != '') {
        currentLength.textContent = count;
      }
      if (input.value.length === parseInt(maxLength, 10)) {
        charCount.classList.add('char-limit');
      }
      
      input.addEventListener('input', () => {
        const count = input.value.length;
        currentLength.textContent = count;
        
        // 入力された文字数が最大文字数に達した場合
        if (count === parseInt(maxLength, 10)) {
          charCount.classList.add('char-limit');
        } else {
          charCount.classList.remove('char-limit');
        }
      });
    
    });
  });
}
