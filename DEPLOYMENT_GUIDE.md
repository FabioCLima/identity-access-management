# Coffee Shop API - Deployment Guide

## Overview

This guide covers deploying the Coffee Shop API to various cloud platforms.

## Deployment Options

### 1. Heroku (Easiest - Recommended)

#### Why Heroku?
- Simple deployment process
- Free tier available
- Automatic SSL
- Easy environment variable management

#### Prerequisites
- Heroku account (free at heroku.com)
- Heroku CLI installed
- Git repository

#### Deployment Steps

**Step 1: Install Heroku CLI**
```bash
# Ubuntu/Debian
curl https://cli-assets.heroku.com/install.sh | sh

# macOS
brew install heroku/brew/heroku

# Or download from https://devcenter.heroku.com/articles/heroku-cli
```

**Step 2: Login to Heroku**
```bash
heroku login
```

**Step 3: Create Heroku App**
```bash
cd ~/Workdir/udacity_projects/identity-access-management/coffee-shop/backend
heroku create coffee-shop-api
```

**Step 4: Create Procfile**
Create `backend/Procfile`:
```
web: gunicorn src.api:app
```

**Step 5: Add Buildpack**
```bash
heroku buildpacks:set heroku/python
```

**Step 6: Set Environment Variables**
```bash
heroku config:set AUTH0_DOMAIN=your-domain.auth0.com
heroku config:set AUTH0_API_AUDIENCE=coffee-shop-api
heroku config:set AUTH0_ALGORITHM=RS256
```

**Step 7: Deploy**
```bash
git push heroku main
```

**Step 8: Open App**
```bash
heroku open
```

### 2. AWS Elastic Beanstalk

#### Why Elastic Beanstalk?
- More control
- Better for production
- AWS ecosystem integration

#### Prerequisites
- AWS account
- EB CLI installed

#### Deployment Steps

**Step 1: Install EB CLI**
```bash
pip install awsebcli
```

**Step 2: Initialize EB**
```bash
cd backend
eb init coffee-shop-api
# Select region
# Select Python 3.11
```

**Step 3: Create Environment**
```bash
eb create coffee-shop-env
```

**Step 4: Set Environment Variables**
```bash
eb setenv AUTH0_DOMAIN=your-domain.auth0.com
eb setenv AUTH0_API_AUDIENCE=coffee-shop-api
```

**Step 5: Deploy**
```bash
eb deploy
```

**Step 6: Open App**
```bash
eb open
```

### 3. Railway (Modern Alternative)

#### Why Railway?
- Very easy setup
- Good free tier
- Modern UI

#### Deployment Steps

**Step 1: Sign up**
- Go to https://railway.app
- Sign up with GitHub

**Step 2: Create New Project**
- Click "New Project"
- Select "Deploy from GitHub repo"

**Step 3: Connect Repository**
- Select your coffee-shop repo
- Railway auto-detects Flask

**Step 4: Set Environment Variables**
Add in Railway dashboard:
- AUTH0_DOMAIN
- AUTH0_API_AUDIENCE
- AUTH0_ALGORITHM

**Step 5: Deploy**
- Railway auto-deploys
- View logs in dashboard

### 4. Vercel (Frontend Deployment)

#### For Ionic Frontend

**Step 1: Install Vercel CLI**
```bash
npm i -g vercel
```

**Step 2: Build Frontend**
```bash
cd frontend
npm run build
```

**Step 3: Deploy**
```bash
vercel --prod
```

## Configuration Files

### backend/Procfile (Heroku)
```
web: gunicorn src.api:app --bind 0.0.0.0:$PORT
```

### backend/runtime.txt (Heroku)
```
python-3.11.0
```

### backend/.ebextensions/python.config (Elastic Beanstalk)
```yaml
option_settings:
  aws:elasticbeanstalk:application:environment:
    AUTH0_DOMAIN: your-domain.auth0.com
  aws:elasticbeanstalk:container:python:
    WSGIPath: src.api:app
```

## Database Considerations

### For SQLite (Development)
- SQLite works for prototypes
- NOT recommended for production

### For Production (PostgreSQL)

**Heroku PostgreSQL:**
```bash
heroku addons:create heroku-postgresql:hobby-dev
```

**Update requirements.txt:**
```txt
Flask==2.0.0
Flask-SQLAlchemy==2.5.0
psycopg2-binary==2.9.5
```

**Update DATABASE_PATH in models.py:**
```python
DATABASE_PATH = os.environ.get('DATABASE_URL', 'sqlite:///database.db')
```

## Security Checklist

Before deploying:

- [ ] All secrets in environment variables
- [ ] No hardcoded credentials
- [ ] HTTPS enabled (automatic with Heroku)
- [ ] CORS configured for production domain
- [ ] Database backups configured
- [ ] Error logging configured
- [ ] Monitoring enabled

## Post-Deployment

### 1. Test Endpoints
```bash
curl https://your-app.herokuapp.com/drinks
```

### 2. Update Auth0 Allowed URLs
- Go to Auth0 Dashboard
- Add production URL to allowed callback URLs

### 3. Update Frontend
Update `frontend/src/environments/environment.prod.ts`:
```typescript
export const environment = {
  apiServerUrl: 'https://your-app.herokuapp.com',
  auth0Domain: 'your-domain.auth0.com',
  auth0ClientId: 'your-client-id',
};
```

## Monitoring

### Heroku Logs
```bash
heroku logs --tail
```

### Health Check Endpoint
Add to `src/api.py`:
```python
@app.route('/health', methods=['GET'])
def health_check():
    return jsonify({
        "status": "healthy",
        "database": "connected"
    }), 200
```

## Cost Comparison

| Platform | Free Tier | Paid Tier |
|----------|-----------|-----------|
| Heroku | 550 hours/month | $7-25/month |
| Railway | 500 hours/month | $5-20/month |
| AWS EB | Limited free | ~$20/month |
| Vercel | Unlimited | $20/month |

## Troubleshooting

### Common Issues

**1. App crashes on startup**
- Check logs: `heroku logs --tail`
- Verify environment variables
- Check database connection

**2. Database errors**
- Ensure PostgreSQL addon is added
- Check DATABASE_URL is set
- Run migrations

**3. Auth0 errors**
- Verify callback URLs in Auth0
- Check CORS settings
- Verify API audience

## Next Steps

1. Choose a platform
2. Create account
3. Deploy backend
4. Deploy frontend
5. Update environment configs
6. Test everything
7. Share live demo!

## Resources

- Heroku Docs: https://devcenter.heroku.com/articles/getting-started-with-python
- Railway Docs: https://docs.railway.app
- AWS EB Docs: https://docs.aws.amazon.com/elasticbeanstalk/
- Vercel Docs: https://vercel.com/docs

