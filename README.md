# Cordova project

Build debug version

``` shell
cordova create cordova-demo com.example.cordovaDemo cordovaDemo
cordova platform add android --save
cordova requirements android 

cordova build android
```

Build release version
``` shell

# Build
cordova build android --release

# Sign
keytool -genkey -v -keystore release-key.keystore -alias cordova-demo -keyalg RSA -keysize 2048 -validity 10000

jarsigner -verbose -sigalg SHA1withRSA -digestalg SHA1 -keystore release-key.keystore android-apk/android-release-unsigned.apk cordova-demo

# Align
zipalign -v 4 android-apk/android-release-unsigned.apk android-apk/cordova-demo.apk

# Automatic
cordova build android --release -- --keystore="release-key.keystore" --alias=cordova-demo --storePassword=testing --password=testing2

```

With json config

``` json
{
  "android": {
    "release": {
      "keystore": "release-key.keystore",
      "alias": "cordova-demo",
      "storePassword": "testing",
      "password": "testing2"
    }
  }
}
```

[Reference](https://blog.csdn.net/frank_wu/article/details/53615165)

## Error: No Java files found that extend CordovaActivity.

cd cordova-src
cordova platform remove android
cordova platform add android

