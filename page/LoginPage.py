from selene.support import by
from selene.support.jquery_style_selectors import s

userNameLocator = s(by.name('user-name'))
userPasswordLocator = s(by.name('password'))
loginBtnLocator = s(by.name('login-button'))