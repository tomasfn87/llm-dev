I need a JavaScript ES5 function code that validates if a string is:
- 1) an email link;
- 2) a telephone number link;
- 3) a social media link that may or **not** have either protocol section (https:// or http://) or the default/main subdomain (www.):
  - :warning: social media must include WhatsApp links (api.whatsapp.com/send?phone= or wa.me/ URLs);
  - optimize social media regular expression to not repeat the '.com' particle.
- do not skip lines or add comments of any kind;
- add 'export default ' before 'function';
- function name = 'isValidEmailPhoneOrSocialMediaUrl'.