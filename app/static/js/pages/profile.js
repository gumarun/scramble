'use strict';

import { truncateText } from '../common/components/truncate.js';
import { toggleIconState } from '../common/components/toggle_icon.js';

truncateText('.profile-link', 23);
truncateText('.post .user-name', 15);
truncateText('.post .user-id', 20);
toggleIconState(".icon-toggle img");


// アイコン状態の切り替え
const detail_icons = document.querySelectorAll(".profile-details img");
const locationElm = document.querySelector(".location-value");
const LinkElm = document.querySelector(".profile-link");
const locationValue = locationElm.textContent.trim();
const linkValue = LinkElm.textContent.trim();

// アイコン状態の切り替え
const values = {
  location: locationValue,
  link: linkValue
};

detail_icons.forEach(function(icon) {
  const id = icon.getAttribute("data-id");
  const defaultSrc = "/static/images/" + id + ".svg";
  const activeSrc = "/static/images/" + id + "_active.svg";
  
  if (values[id] != "") {
    icon.setAttribute("src", activeSrc);
  } else {
    icon.setAttribute("src", defaultSrc);
  }
});
