
# imports
from instapy import InstaPy
from instapy import smart_run

# login credentials
insta_username = '****'
insta_password = '****'

comments = ['Nice shot! @{}',
        'I love your profile! @{}',
        'Your feed is an inspiration :thumbsup:',
        'Just incredible :open_mouth:',
        'What camera did you use @{}?',
        'Love your posts @{}',
        'Looks awesome @{}',
        'Getting inspired by you @{}',
        ':raised_hands: Yes!',
        'I can feel your passion @{} :muscle:'
        u"Nice!😜",
       u"Sweet!😘", 
       "Beautiful :heart_eyes:"]
tags = ['engineer','big bumps','natgeo','biomedical','KU','python programming','BMW','INTERNET OF THINGS','fashion','web development']

# get an InstaPy session!
# set headless_browser=True to run InstaPy in the background
session = InstaPy(username=insta_username,
                  password=insta_password,
                  headless_browser=True,
                  bypass_security_challenge_using='email',
                  want_check_browser=False)

with smart_run(session):
  """ Activity flow """		
  # general settings		
  #session.set_dont_include(["friend1", "friend2", "friend3"])		
  session.set_action_delays(enabled=True,follow=2)
  # activity		
  #session.like_by_tags(["natgeo"], amount=10)

  # Joining Engagement Pods
  #session.set_do_comment(enabled=True, percentage=35)
 # session.set_comments(comments)
  #session.set_do_reply_to_comments(enabled=True, percentage=14)
 # session.set_comment_replies(replies=[u"😎😎😎", u"😁😁😁😁😁😁😁💪🏼", u"😋🎉", "😀🍬", u"😂😂😂👈🏼👏🏼👏🏼", u"🙂🙋🏼‍♂️🚀🎊🎊🎊", u"😁😁😁", u"😂",  u"🤓🤓🤓🤓🤓",u"👏🏼😉"],media="Photo")

  #session.join_pods(topic='sports', engagement_mode='no_comments')
  session.follow_by_tags(tags,amount=2)
  session.end()

