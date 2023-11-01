function changePage(pageName) {
  if (pageName === 'Home') {
    window.location.href = '../index.html';
  } else if (pageName === 'Ho') {
    window.location.href = '../ho/index.html';
  } else if (pageName === 'happy') {
    window.location.href = '../happy/index.html';
  } else if (pageName === 'example') {  // 只有當前分頁路徑是 ./ ; 其他都是 ../ 因為要回根目錄
    window.location.href = './index.html';
  }
}
