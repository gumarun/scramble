'use strict';

// フラッシュメッセージのカテゴリを基に該当するフィールドにエラークラスを追加
function processFlashMessages(flashMsg, errorMappings) {
  if (!flashMsg) return;

  flashMsg.forEach(msg => {
    // カテゴリとしてクラス名を取得
    const category = msg.className;
    // エラーカテゴリとフィールドセレクタのマッピングに基づいて処理
    Object.entries(errorMappings).forEach(([errorClass, fieldSelector]) => {
      if (!category.includes(errorClass)) return;

      // 対象フィールドを取得
      const field = document.querySelector(fieldSelector);
      if (!field) return;

      // フィールドの親要素にエラークラスを追加
      const wrap = field.closest('.form-input-wrap');
      if (wrap) {
        wrap.classList.add('error-border');
      }
    });
  });
}

// エラーテキスト要素を取得し、空でないテキストがあればエラーフラグを立てる
function handleErrorTexts(wrap) {
  const errorTexts = wrap.parentElement.querySelectorAll('.error-text');
  
  let hasError = false;
  
  errorTexts.forEach(txt => {
    if (txt.textContent.trim() === '') {
      txt.remove();
    } else {
      hasError = true;
    }
  });
  
  return { errorTexts, hasError };
}

// エラーフラグがあれば、親要素にエラークラスを追加
function applyErrorClass(wrap, hasError) {
  if (hasError) {
    wrap.classList.add('error-border');
  }
}

// 入力時にエラークラスを外す処理
function removeErrorClass(input, wrap, errorTexts) {
  if (!input) return;
  
  input.addEventListener('input', () => {
    wrap.classList.remove('error-border');
    errorTexts.forEach(txt => txt.classList.add('hidden'));
  });
}

// バリデーションのスタイルを適用するメイン関数
export function setupValidationStyles() {
  const inputWraps = document.querySelectorAll('.form-input-wrap');
  const flashMessage = document.querySelectorAll('.flash-message');
  
  // フラッシュメッセージとフィールドの紐づけ
  const errorMappings = {
    'user-id-error': '.user-id',
    'username-error': '.user-name',
  };
  processFlashMessages(flashMessage, errorMappings);
  
  inputWraps.forEach(wrap => {
    // 各input要素
    const input = wrap.querySelector('.form-input');
    // エラーフラグがあればエラーテキストを取得
    const { errorTexts, hasError } = handleErrorTexts(wrap);
    
    // エラーがあればエラークラスを追加
    applyErrorClass(wrap, hasError);
    // 入力時にエラークラスを削除
    removeErrorClass(input, wrap, errorTexts);
  });
}
