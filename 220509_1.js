var speaker = {
    firstName: 'Jeon',
    lastName: 'Seokhwan',
    email: 'maninblakc87@naver.com',
    about: 'um.. hello! my name is what is the matter?',
    company: 'JeonCom',
    tags: ['stupid', 'stupid', 'stupid', 'web design', 'I wanna programmer'],
    registered: true
}

function serializeSpeaker(key, value) {
    return (typeof value === 'string' || Array.isArray(value)) ? undefined : value;
}

console.log(JSON.stringify(speaker, null, 2) + '\n');

console.log(JSON.stringify(speaker, serializeSpeaker, 2));