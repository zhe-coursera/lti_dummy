**Do not use this in any production as is. This will log secret key by default.**

*modified from https://github.com/mitodl/mit_lti_flask_sample*

# lti_dummy
Simple LTI tool that returns a grade. Useful for debugging &amp; development.

## Install & start local server
```
git clone git@github.com:zhe-coursera/lti_dummy.git
cd lti_dummy
pip install -r requirements.txt
python lti_flask.py
```

Then navigate to [http://localhost:5000/is_up](http://localhost:5000/is_up)

If you see a page containing the words, "I'm up", you have verified that you
can run the sample app locally.

## Set up on coursera
* create an LTI from authoring
* Launch URL: `http://localhost:5000/`
* Consumer Key: `__consumer_key__`
* Secret: `__lti_secret__`

*Consumer Key and Secret can be customized in `config.py`*

## Testing on coursera
* view LTI as learner
* click open and put in a grade
* refresh LTI page on coursera, and the grade should show up

*By default coursera.org takes the highest grade as the LTI grade. For example, for the same item, a learner get 0.3 at the first try and 0.2 at the second, the grade will remain to be 0.3*
