'use strict';

export function setupSegment() {
  // 現在ページのパスをセグメントで分割
  const pathSegments = window.location.pathname.split('/')

  // 空白を除いて最後のセグメントを取得
  const lastSegment = pathSegments.filter(seg => seg !== '').pop();

  // main要素を取得
  const mainElement = document.querySelector('main');

  // 取得したセグメント（パス名）をclass名としてbodyに追加
  if (!lastSegment) {
    mainElement.classList.add('page-home');
  } else {
    mainElement.classList.add(`page-${lastSegment}`);
  }
}
