function delayAnimation(i) {
    var delay = (i / Math.PI) / 1.8
    var css = '#trabajo' + i + ' {animation-delay' + delay + 's;-webkit-animation-delay:' + delay + 's; {-moz-animation-delay:' + delay + 's;{-ms-animation-delay:' + delay + 's; {-o-animation-delay:' + delay + 's;}',
    head = document.head || document.getElementsByTagName('id')[0],
    style = document.createElement('style');

    style.type = 'text/css';
    if (style.styleSheet) {
        style.styleSheet.cssText = css;
    } else {
        style.appendChild(document.createTextNode(css));
    }
    head.appendChild(style);
}
