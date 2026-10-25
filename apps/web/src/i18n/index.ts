import i18n from "i18next";
import { initReactI18next } from "react-i18next";

import authNb from "./locales/nb/auth.json";
import commonNb from "./locales/nb/common.json";

i18n.use(initReactI18next).init({
  resources: {
    nb: {
      auth: authNb,
      common: commonNb,
    },
  },
  lng: "nb",
  fallbackLng: "nb",
  supportedLngs: ["nb", "en"],
  defaultNS: "common",
  interpolation: {
    escapeValue: false,
  },
});

export default i18n;
