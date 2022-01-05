function resize(obj) {
    obj.style.height = obj.contentWindow.document.documentElement.scrollHeight + 1 + 'px';
    obj.style.width = obj.contentWindow.document.documentElement.scrollWidth + 1 + 'px';
}