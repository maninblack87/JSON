var speaker = {
    firstName: 'Jeon',
    lastName: 'Seokhwan',
    email: 'maninblakc87@naver.com',
    about: 'um.. hello! my name is what is the matter?',
    company: 'JeonCom',
    tags: ['stupid', 'stupid', 'stupid', 'web design', 'I wanna programmer'],
    registered: true
};

speaker.toJSON = function () {
    return "Hi there!";
}

console.log(JSON.stringify(speaker, null, 2));