# Auth0 Multi-Factor Authentication Setup

## Overview

Add Multi-Factor Authentication (MFA) and social login to enhance security and user experience.

## Why Add MFA?

- **Security:** Extra layer of protection
- **Best Practice:** Industry standard
- **User Experience:** Modern authentication flow
- **Project Highlight:** Shows advanced IAM understanding

## Step 1: Enable MFA in Auth0

1. Go to Auth0 Dashboard
2. Navigate to **Security → Multi-factor Auth**
3. Enable desired MFA methods:
   - **SMS** (easiest for testing)
   - **Authenticator Apps** (TOTP)
   - **Email** (can enable all)

### Configure SMS MFA

1. Click **SMS** in MFA section
2. Configure provider (Twilio recommended)
3. Add phone number verification template

### Configure Authenticator App MFA

1. Click **OTP** in MFA section
2. Enable TOTP (Time-based One-Time Password)
3. Configure issuer name: "Coffee Shop"

## Step 2: Enable MFA Per Application

1. Go to **Applications**
2. Select your Coffee Shop application
3. Go to **Multifactor Auth** tab
4. Enable required MFA factors

## Step 3: Add Social Login

### Enable Social Connections

1. Go to **Authentication → Social**
2. Enable providers:
   - **Google** (easiest)
   - **GitHub** (developer-friendly)
   - **Facebook** (optional)

### Configure Google Login

1. Click **Google**
2. Click **"Create Application"**
3. Add credentials from Google Cloud Console
4. Configure:
   - Allowed Callback URLs
   - Allowed Logout URLs

## Step 4: Update Backend Code

No changes needed! Auth0 handles MFA automatically.

## Step 5: Test MFA Flow

### User Registration with MFA

1. User signs up
2. User verifies email (if enabled)
3. User is prompted for MFA
4. User enters code from SMS/Authenticator
5. User receives access token

### User Login with MFA

1. User enters credentials
2. Auth0 verifies credentials
3. Auth0 sends MFA challenge
4. User enters MFA code
5. Auth0 returns token

## Step 6: Handle MFA in Frontend

Update `frontend/src/app/services/auth.service.ts`:

```typescript
async loginWithMFA() {
  try {
    // Auth0 SDK handles MFA automatically
    const result = await this.auth0.loginWithRedirect({
      screen_hint: 'signup'
    });
    
    // User completes MFA during login
    // Token received after MFA verification
    
    return result;
  } catch (error) {
    console.error('MFA login error:', error);
    throw error;
  }
}

async handleMFACallback() {
  // Auth0 SDK handles MFA callback
  const result = await this.auth0.handleRedirectCallback();
  return result;
}
```

## Step 7: Add Social Login Buttons

Update login page template:

```html
<ion-content class="login-content">
  <div class="login-container">
    <h1>Welcome to Coffee Shop</h1>
    
    <!-- Email/Password Login -->
    <ion-button expand="block" (click)="login()">
      Sign In
    </ion-button>
    
    <!-- Social Login -->
    <ion-button expand="block" color="danger" (click)="loginWithGoogle()">
      <ion-icon name="logo-google" slot="start"></ion-icon>
      Sign In with Google
    </ion-button>
    
    <ion-button expand="block" (click)="loginWithGitHub()">
      <ion-icon name="logo-github" slot="start"></ion-icon>
      Sign In with GitHub
    </ion-button>
  </div>
</ion-content>
```

## Step 8: Environment Variables

Add to frontend environment:

```typescript
export const environment = {
  auth0Domain: 'your-domain.auth0.com',
  auth0ClientId: 'your-client-id',
  auth0Audience: 'coffee-shop-api',
  // MFA is handled by Auth0
};
```

## Step 9: Update User Profile

Add MFA enrollment prompt for administrators:

```typescript
async enforceMFA() {
  // Check if user has MFA enrolled
  const hasMFA = await this.checkUserMFA();
  
  if (!hasMFA) {
    // Prompt user to enroll
    this.showMFAEnrollmentPrompt();
  }
}
```

## Testing Checklist

- [ ] Test SMS MFA flow
- [ ] Test Authenticator App MFA flow
- [ ] Test Google login
- [ ] Test GitHub login
- [ ] Test MFA enforcement
- [ ] Test token refresh with MFA
- [ ] Test on mobile devices

## User Experience Flow

### First Time User
1. User clicks "Sign Up"
2. User chooses: Email or Social
3. User completes MFA enrollment
4. User redirected to app
5. User can access based on role

### Returning User
1. User clicks "Sign In"
2. User enters credentials
3. User completes MFA challenge
4. User redirected to app
5. User can access based on role

## Benefits

- **Enhanced Security:** Two-factor protection
- **User Choice:** Multiple login options
- **Modern UX:** Industry-standard authentication
- **Project Highlight:** Shows IAM expertise
- **Professional:** Production-ready authentication

## Estimated Time

- Auth0 configuration: 1 hour
- Social login setup: 1 hour
- Frontend integration: 2 hours
- Testing: 1 hour
- **Total: 5 hours**

## Resources

- Auth0 MFA Docs: https://auth0.com/docs/mfa
- Social Logins: https://auth0.com/docs/connections
- Angular Auth0 SDK: https://github.com/auth0/auth0-angular

