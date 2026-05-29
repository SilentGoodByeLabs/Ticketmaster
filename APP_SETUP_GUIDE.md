
# Ticketmaster Demo App Setup Guide for Appy Pie

## 1. App Configuration (IMPORTANT!)

### App Name
- **Change to**: Ticketmaster Demo
- Make sure it's not "Ticketphantom" or anything else!

### App ID / Package Name
- **Android**: com.ticketmaster.demo
- **iOS**: com.ticketmaster.demo

## 2. App Icon

### How to add our T logo:
1. Download or use our `logo.svg` from this folder
2. In Appy Pie, go to **Design > App Icon**
3. Upload `logo.svg` or convert it to PNG first (512x512 pixels is best)

The logo is a blue square with a white "T" - just like Ticketmaster's!

## 3. App Content

### Website/Web App URL
1. In Appy Pie, select "Website" or "Web App" as your app type
2. Use this as your main page: **index.html** from our `www` folder

### What the App Includes:
- Event listing page (4 sample events)
- Ticket booking form
- Fake payment flow (demo only - no real money!)
- Booking confirmation screen
- All styled like Ticketmaster!

## 4. How to Get IPA File for iPhone (iOS)
To get an iOS build from Appy Pie:
1. Make sure you have an **Apple Developer Account** ($99/year)
2. In Appy Pie, go to **Publish > iOS**
3. Follow the steps to upload your iOS certificates
4. Appy Pie will generate the IPA file for you
5. You can install it on iPhones using TestFlight or directly

## 5. Our Files
- `www/index.html` - Main app page (use this in Appy Pie!)
- `www/logo.svg` - App icon
- `capacitor.config.ts` - Capacitor configuration (if you use Capacitor instead of Appy Pie)

## 6. Demo Features
- Click any event to book tickets
- Enter name, email, number of tickets
- Choose a payment method (it's all fake!)
- See a confirmation message with ticket details
- NO real payment information is collected!

That's it! Your app should now be named "Ticketmaster Demo" and have the proper T logo!
