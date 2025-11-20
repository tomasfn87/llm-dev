import isValidEmailPhoneOrSocialMediaUrl from './isValidEmailPhoneOrSocialMediaUrl.js'; 
import { color } from './utils/color.js'; 

const main = () => {
    [
        "mailto:test@test.ing",
        "tel:+1234567890",
        "https://twitter.com/testuser",
        "https://www.facebook.com/testuser",
        "https://wa.me/+1234567890",
        "https://api.whatsapp.com/send?phone=+1234567890",
        "instagram.com/testuser",
        "invalid-email@.com",
        "12345",
        "https://notasocialmedia.com/user",
        "test"
    ].forEach(e => {
        isValidEmailPhoneOrSocialMediaUrl(e)
            ? color.log('green', ' Ok ')
            : color.log('red', 'Fail');
        color.log('dim', " - ");
        isValidEmailPhoneOrSocialMediaUrl(e)
            ? process.stdout.write(e)
            : color.log('brightMagenta', e);
        console.log();
    });
};

main();
