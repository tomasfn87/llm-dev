export default function isValidEmailPhoneOrSocialMediaURL(str) {
if (typeof str !== 'string' || str.length === 0) return false;
var re = new RegExp(
  "^(?:mailto:[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\\.[a-zA-Z]{2,}" +
  "|tel:\\+?[\\d\\s\\-()]{7,20}" +
  "|(?:https?://)?(?:www\\.)?" +
  "(?:api\\.whatsapp\\.com/send\\?phone=[\\d+]+|" +
  "wa\\.me/[\\d+]+|" +
  "(?:facebook|instagram|twitter|linkedin|pinterest|tiktok|youtube|snapchat|reddit|tumblr)\\.com(?:/[^\\s]*)?)" +
  ")$"
);
return re.test(str);
}
