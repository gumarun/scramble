'use strict';

// ユーザーIDの入力パターンを制限
const userIdInput = document.getElementById('user_id');

userIdInput.addEventListener('focus', function() {
  userIdInput.setAttribute('inputmode', 'latin');
  userIdInput.setAttribute('lang', 'en');
});

userIdInput.addEventListener('input', function() {
  this.value = this.value.replace(/[^A-Za-z0-9_]/g, '');
});


// スペースの入力を禁止
const inputs = document.querySelectorAll('.form-item-group input');
inputs.forEach(input => {
  input.addEventListener('keydown', (event) => {
    if (event.key === ' ') {
      event.preventDefault();
    }
  });
});


// inputフォーカス時のactive処理
inputs.forEach(input => {
  const placeholder = input.previousElementSibling;

  // フォーカスした時
  input.addEventListener('focus', () => {
    input.classList.add('active')
    placeholder.classList.add('active');
  });

  // フォーカスが外れた時
  input.addEventListener('blur', () => {
    if (input.value === '') {
      input.classList.remove('active')
      placeholder.classList.remove('active');
    }
  });
});
