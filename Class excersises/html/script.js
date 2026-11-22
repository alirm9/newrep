"use strict";
console.log("this text is from the console");
console.log("Howdy partner!");
let number, name;
number = 153;
name = "Anna";
console.log(number);
console.log(name);
number = -17;
name = "Pekka";
console.log(number);
console.log(name);
console.log(typeof number);
const names = "Ahmed";
console.log(typeof names);
console.log(names);
const age = 23;
const ageString = age.toString();
const btn = document.querySelector("#myBtn");
const output = document.querySelector("#output");

// ۲. اتصال شنونده رویداد (Event Listener)
btn.addEventListener("click", function (evt) {
  output.innerText = "Button was clicked!";
  console.log(evt.target); // دقیقاً همان دکمه‌ای که کلیک شده را نشان می‌دهد
});

// ۱. تعریف تابع غیرهمگام با کلمه async
async function fetchData() {
  // ۲. بلوک try برای اجرای کدی که ممکن است خطای شبکه بدهد
  try {
    // ۳. ارسال درخواست به سرور و صبر کردن (await) برای دریافت پاسخ اولیه (Headers/Status)
    const response = await fetch("https://api.tvmaze.com/search/shows?q=emmerdale");

    // ۴. چک کردن موفقیت‌آمیز بودن پاسخ HTTP (کدهای 200 تا 299)
    // نکته مهم: fetch در خطاهای 404 یا 500 وارد catch نمی‌شود! خودمان باید چک کنیم:
    if (!response.ok) {
      throw new Error("HTTP error! status: " + response.status);
    }

    // ۵. تبدیل بدنه پاسخ از متن JSON به آرایه/شیء جاوااسکریپت (این مرحله هم زمان‌بر است و await می‌خواهد!)
    const data = await response.json();

    // ۶. استفاده از داده‌ها (مثلاً چاپ در کنسول یا نمایش در DOM)
    console.log("Fetched data:", data);
    return data;

  } catch (error) {
    // ۷. اگر اینترنت قطع بود یا throw new Error اجرا شد، برنامه به اینجا می‌پرد
    console.error("Error fetching data:", error);
  }
}

// ۸. فراخوانی تابع
fetchData();
console.log("This message is printed before the data is fetched");