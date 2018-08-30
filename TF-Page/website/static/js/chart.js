function chartAnimation(id,texto,color,percentage){
    var fillPercentage = (percentage / 100) * 180;
    var css = '#' + id + ' li:nth-child(1) { z-index: 1; border-color:' + color +'; animation-name: rotate-one; animation-delay: 1.1s}'+
              '#'+id+' li:nth-child(1) span {top: 5px;left: 10px;transform: rotate(-'+fillPercentage+'deg);}'+
              '@keyframes rotate-one { 100% {transform: rotate('+fillPercentage+'deg); } }';
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