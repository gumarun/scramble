'use strict';

//入力フィールドの active クラスを制御
export function toggleActiveClass() {
  const inputWraps = document.querySelectorAll('.form-input-wrap');
  
  inputWraps.forEach(wrap => {
    const inputs = wrap.querySelectorAll('input, textarea');
    inputs.forEach(input =>{
      // 初期状態で文字がある場合
      if (input.value.trim() !== '') {
        wrap.classList.add('active');
      }
      // フォーカスした場合
      input.addEventListener('focus', () => {
        wrap.classList.add('active');
      });
      // フォーカスが外れた場合
      input.addEventListener('blur', () => {
        if (input.value.trim() === '') {
          wrap.classList.remove('active');
        }
      });
    });
  });
}
