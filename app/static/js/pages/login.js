import { removeSpaces } from "../common/utils/form/sanitize.js";
import { setupValidationStyles } from "../common/utils/form/validation.js";
import { toggleActiveClass } from "../common/utils/form/activeClass.js";

setupValidationStyles();
removeSpaces();
toggleActiveClass();