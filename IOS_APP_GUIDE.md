# Guide to Building an iOS .ipa for Your Ticketmaster Website

## What You'll Need
1. A Mac computer (for Xcode)
2. An Apple ID (free or paid developer account)
3. Your website files (already prepared in this folder)

---

## Step 1: Prepare Your Website Files
First, make sure your website files are in a folder called `www`. The structure should look like this:
```
www/
├── index.html
├── uk.tmconst.com/
├── s1.ticketm.net/
└── prismic-images.tmol.io/
```

---

## Step 2: Set Up Capacitor on macOS

### 2.1 Install Node.js (if not already installed)
Download from: https://nodejs.org/

### 2.2 Open Terminal and Navigate to Your Project Folder
```bash
cd /path/to/your/www.ticketmaster.com
```

### 2.3 Install Capacitor
```bash
npm install @capacitor/core @capacitor/cli @capacitor/ios
```

### 2.4 Initialize Capacitor
```bash
npx cap init "Ticketmaster" "com.ticketmaster.app"
```

### 2.5 Add iOS Platform
```bash
npx cap add ios
```

### 2.6 Sync Your Website Files
```bash
npx cap sync
```

---

## Step 3: Open the Project in Xcode
```bash
npx cap open ios
```

---

## Step 4: Configure Your App in Xcode
1. In Xcode, select your project in the left sidebar
2. Go to the "Signing & Capabilities" tab
3. Select your team (Apple ID)
4. Make sure "Automatically manage signing" is checked

---

## Step 5: Build and Export the .ipa
1. In Xcode, select "Any iOS Device (arm64)" as the build target
2. Go to **Product → Archive**
3. Once archived, click "Distribute App"
4. Choose "Ad Hoc" or "Development" for distribution
5. Follow the prompts to export the .ipa file

---

## Step 6: Sideload with Sideloadly
1. Download Sideloadly from: https://sideloadly.io/
2. Open Sideloadly
3. Connect your iPhone to your Mac
4. Drag and drop your .ipa file into Sideloadly
5. Enter your Apple ID and password
6. Click "Start" to install

---

## Troubleshooting
- **Signing Errors**: Make sure your Apple ID is valid and you've trusted the developer profile on your iPhone (Settings → General → VPN & Device Management)
- **Website Not Loading**: Double-check that all files are in the `www` folder and `npx cap sync` was run
