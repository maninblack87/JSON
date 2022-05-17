var xhr = new XMLHttpRequest();
var url = 'http://apis.data.go.kr/1192000/select0040List/getselect0040List'; /*URL*/
var queryParams = '?' + encodeURIComponent('serviceKey') + '='+'서비스키'; /*Service Key*/
queryParams += '&' + encodeURIComponent('numOfRows') + '=' + encodeURIComponent('10'); /**/
queryParams += '&' + encodeURIComponent('pageNo') + '=' + encodeURIComponent('1'); /**/
queryParams += '&' + encodeURIComponent('type') + '=' + encodeURIComponent('xml'); /**/
queryParams += '&' + encodeURIComponent('baseDt') + '=' + encodeURIComponent('20210101'); /**/
queryParams += '&' + encodeURIComponent('mxtrNm') + '=' + encodeURIComponent('옹진수산업협동조합'); /**/
queryParams += '&' + encodeURIComponent('csmtmktNm') + '=' + encodeURIComponent('연안위판장(옹진)'); /**/
queryParams += '&' + encodeURIComponent('mprcStdCode') + '=' + encodeURIComponent('620401'); /**/
queryParams += '&' + encodeURIComponent('mprcStdCodeNm') + '=' + encodeURIComponent('굴(참굴)'); /**/
xhr.open('GET', url + queryParams);
xhr.onreadystatechange = function () {
    if (this.readyState == 4) {
        alert('Status: '+this.status+'nHeaders: '+JSON.stringify(this.getAllResponseHeaders())+'nBody: '+this.responseText);
    }
};

xhr.send('');