'use strict';

// バリエーションエラー時のスタイルの制御
function applyValidationStyles (wrap, flashMessage) {
  // 各formアイテムの子要素を取得
  const input = wrap.querySelector('.form-input');
  const errorTexts = wrap.querySelectorAll('.error-text');

  // 初期状態でエラーメッセージがあればエラークラスを付与
  errorTexts.forEach(txt => {
    if (txt) {
      wrap.classList.add('error-border');
    }
  });
  
  // 該当するフィールドにエラークラスを付与
  if (flashMessage) {
    flashMessage.forEach(msg => {
      const category = msg.className;
      if (category.includes("user-id-error")) {
        const idField = document.querySelector('.user-id');
        const idWrap = idField.closest('.form-input-wrap');
        idWrap.classList.add('error-border');
      }
      if (category.includes("username-error")) {
        const nameField = document.querySelector('.user-name');
        const nameWrap = nameField.closest('.form-input-wrap');
        nameWrap.classList.add('error-border');
      }
    });
  }
  
  // 入力時にエラークラスを外す
  input.addEventListener('input', () => {
    if (wrap.classList.contains('error-border')) {
      wrap.classList.remove('error-border');
      errorTexts.forEach(txt => { txt.classList.add('hidden'); });
    }
  });
}

export function setupValidationStyles() {
  const inputWraps = document.querySelectorAll('.form-input-wrap');
  const flashMessage = document.querySelectorAll('.flash-message');

  inputWraps.forEach(wrap => {
    applyValidationStyles (wrap, flashMessage);
  });
}
