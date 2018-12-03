# bodycalc.io

## Deployment shortcuts
- Compile and run locally:
```
source .env3/bin/activate
cd django
python manage.py collectstatic
python manage.py runserver
```

- Deploy to AWS Lambda:
```
source .env3/bin/activate
cd django
zappa update dev
```
- Sync static assets to AWS S3:
```
aws s3 sync static/ s3://bodycalc.io/static/
```


## Environment and Infrastructure Setup
- API Gateway End points:
  - https://bodycalc.io
  - https://d29xo46q0sqnzl.cloudfront.net
  - https://co29zf6w3f.execute-api.us-west-2.amazonaws.com/dev
- IAM user: bodycalc.io
- S3: https://s3-us-west-2.amazonaws.com/bodycalc.io/static/
- Cloudfront:
  - https://cdn.bodycalc.io
  - https://d2aeb81h32shl0.cloudfront.net
- Bootstrap UI Theme
  - https://themes.getbootstrap.com/product/keen-the-ultimate-bootstrap-admin-theme/
  - Docs: keen_v1.3.1/docs/docs.html


### Django Build
- To do: https://bower.io/blog/2017/how-to-migrate-away-from-bower/
```
pip install awscli
source .env3/bin/activate
django-admin startproject app   # create a new project named app
cd app
python manage.py runserver  # to verify that django installed and initialized correctly
python manage.py startapp bmi   # create the BMI web app
pip install -r requirements.txt
python manage.py bower install
```

### Zappa AWS deployment manager setup
- Note that Zappa relies an IAM user which is specified in django.zappa_settings.json. I placed a copy of the IAM policy in json format in aws-iam-policy.json.
- When I had to manually add the VPC settings to zappa_settings.json. I never figured out the individual policy permissions for this and so ended up temporarily adding admin rights to the project's IAM user.
- Ensure that the RDS MySQL database uses IAM access rather than traditional username / pwd.

* Manual deployment steps
  * Enable CORS in AWS API Gateway. this is necessary for Fontawesome files.
  * add VPC settings to zappa_settings.json

```
zappa init         # see notes below on installation details
zappa deploy dev   # Deploy app to AWS
zappa undeploy dev # Delete from AWS
zappa update dev   # update existing app to AWS
zappa manage dev "collectstatic --noinput"    # collect static assets
zappa tail         # view Lambda execution log
zappa -h
```

### Stack References
* Django: https://www.djangoproject.com/
* Django Environment: https://github.com/joke2k/django-environ
* Using Amazon S3 to Store your Django Site's Static and Media Files: https://www.caktusgroup.com/blog/2014/11/10/Using-Amazon-S3-to-store-your-Django-sites-static-and-media-files/
* Static files - Django Official Documentation: https://docs.djangoproject.com/en/2.1/howto/static-files/
* Django - Zappa Guide: https://edgarroman.github.io/zappa-django-guide/
* Zappa setup: https://blog.apcelent.com/deploy-flask-aws-lambda.html (this is not as useful)
* Django static asset w Zappa: https://docs.djangoproject.com/en/2.1/howto/static-files/



### settings.py
- DATABASES: changed settings to AWS RDS MySQL. config settings are stored locally in mysite/.env
- ALLOWED_HOSTS: added FQDN's for amazon.com and lawrencemcdaniel.com per suggestions in the Django - Zappa Guide
- SECRET_KEY: moved to locally-stored .env file
- DEBUG:  moved to locally-stored .env file
