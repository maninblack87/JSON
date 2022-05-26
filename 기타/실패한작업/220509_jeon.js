var speaker = {
    firstName: 'Jeon',
    lastName: 'Seokhwan',
    email: 'maninblakc87@naver.com',
    about: 'um.. hello! my name is what is the matter?',
    company: 'JeonCom',
    tags: ['stupid', 'stupid', 'stupid', 'web design', 'I wanna programmer'],
    registered: true
}

var json = JSON.parse(speaker);

console.log(json.firstName);