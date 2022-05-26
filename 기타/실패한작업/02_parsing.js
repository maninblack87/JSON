var json = '{' +
    '"firstName": "Larson",' +
    '"lastName": "Richard",' +
    '"email": "larsonrichard",' +
    '"company": "Ecratic",' +
    '"tags": [' +
    '"json",' +
    '"rest",' +
    '"api",' +
    '"oauth"' +
    '],' +
    '"registered": true' +
    '}';

var speaker = JSON.parse(json);

console.log('speaker.firstName = ' + speaker.firstName);