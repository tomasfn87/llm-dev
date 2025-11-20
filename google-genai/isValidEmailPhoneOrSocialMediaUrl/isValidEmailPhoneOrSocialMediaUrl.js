export default function isValidEmailPhoneOrSocialMediaUrl(str) {
  var emailRegex = /^mailto:[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$/;
  var phoneRegex = /^tel:\+?[\d\s\-\(\)]+$/;
  var socialMediaRegex = /^(?:https?:\/\/)?(?:www\.)?(?:(?:facebook|twitter|linkedin|instagram|pinterest|youtube|snapchat|tiktok|reddit|tumblr|vk|flickr)\.com|api\.whatsapp\.com\/send\?phone=\+?[\d]+|wa\.me\/\+?[\d]+)(?:\/[\w\-\.\/~%\+\?&=\#]*)?$/;
  return emailRegex.test(str) || phoneRegex.test(str) || socialMediaRegex.test(str);
}
