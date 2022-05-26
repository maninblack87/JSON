var json = '{' +
    '"firstName": "Jeon",' +
    '"lastName": "Seokhwan",' +
    '"email": "maninblakc87@naver.com",' +
    '"about": "um..hello!mynameiswhatisthematter?",' +
    '"company": "JeonCom",' +
    '"tags": [' +
    '"stupid",' +
    '"stupid",' +
    '"stupid",' +
    '"webdesign",' +
    '"I wanna programmer"' +
    '],' +
    '"registered": true' +
    '}';

var speaker = JSON.parse(json);

console.log(speaker.firstName);