# COM2703 เครือข่ายคอมพิวเตอร์ (Computer Network) - Final Review & Interactive Web Portal

เว็บแอปพลิเคชันสำหรับสรุปเนื้อหาบทเรียน, แฟลชการ์ดทวนคำศัพท์, คลังข้อสอบ Final 90 ข้อ (พร้อมเฉลยละเอียด), และเครื่องมือคำนวณ IPv4 Subnet สำหรับรายวิชา **COM2703 (สื่อสารข้อมูลและเครือข่ายคอมพิวเตอร์)** ครอบคลุม **บทที่ 5 - 8**

🌐 **เข้าใช้งานเว็บ:** [https://cj007zaza.github.io/com2703/](https://cj007zaza.github.io/com2703/)

---

## 🌟 ฟีเจอร์หลักของเว็บแอปพลิเคชัน

### 1. 📚 สรุปเนื้อหาบทเรียนพร้อมภาพประกอบ (Illustrated Summaries)
* **บทที่ 5: โพรโทคอล & OSI Model** - แผนผัง OSI 7-Layer Protocol Map, ตารางเปรียบเทียบ ARP vs RARP, TCP vs UDP, POP3 vs IMAP, Telnet vs SSH, MQTT
* **บทที่ 6: สถาปัตยกรรมเครือข่าย & Routing** - ขอบเขตระยะทาง (PAN, LAN, MAN, WAN), ระบบสลับสาย 3 รูปแบบ (Circuit, Message Store-and-Forward, Packet: Datagram, SVC, PVC), และการเปรียบเทียบเทคนิคการหาเส้นทาง (Routing 5 แบบ)
* **บทที่ 7: ระบบเครือข่าย LAN & Topology** - ไดอะแกรมเวกเตอร์ SVG คมชัดสำหรับ BUS (Terminator & Echo), STAR (Central Switch/Hub Single Point of Failure), RING (FDDI Dual-Ring Backbone), STAR-wire RING (MAU Bypass), MESH (Full Point-to-Point), ตารางเปรียบเทียบข้อดี-ข้อจำกัด, ชนิดของเซิร์ฟเวอร์ (Proxy Web Cache, Disk Server, File Server) และมาตรฐาน Ethernet
* **บทที่ 8: Subnetting & IP Addressing** - ตารางเปรียบเทียบ IPv4 (32 บิต) vs IPv6 (128 บิต), กฎการย่อ IPv6 (`::`), ตาราง Classful A, B, C, D, E, ตารางค่าน้ำหนัก 8 บิต ($128, 64, 32, 16, 8, 4, 2, 1$), สูตร Block size คิดลัด Network/Broadcast IP, และสัญลักษณ์อุปกรณ์ Cisco Packet Tracer (Router, Switch, Hub, Cloud)

### 2. 🗂️ แฟลชการ์ดคำศัพท์ (Vocabulary Flashcards)
* รวบรวมคำศัพท์และนิยามสำคัญกว่า **65+ คำศัพท์** จากบทที่ 5, 6, 7 และ 8
* มีป้ายกำกับบทเรียนชัดเจน เช่น `[บทที่ 5]`, `[บทที่ 6]`, `[บทที่ 7]`, `[บทที่ 8]`
* สามารถคลิกพลิกการ์ด 3D ดูความหมาย พร้อม **สูตรท่องจำสำหรับเข้าห้องสอบ**
* ฟังก์ชันสลับการ์ด (Shuffle), ตัวกรองแยกบท, ปุ่มทำเครื่องหมาย "จำได้แล้ว (Mastered)" และรองรับปุ่มลัดคีย์บอร์ด (Arrow Left/Right, Spacebar)

### 3. ✍️ คลังข้อสอบ Final 90 ข้อ (Final Exam 90 Qs)
* ข้อสอบ 90 ข้อเต็ม ตามโครงสร้างการสอบจริงผ่านระบบ **Socrative 90 ข้อ**
* อ้างอิงจาก **ข้อสอบเก็บคะแนนจริงบทที่ 5-7 (40 ข้อ)** และ **แนวข้อสอบ Final ทบทวน + Assignment 7, 8.1, 8.2 (50 ข้อ)**
* **Practice Mode:** ฝึกทำทีละข้อ พร้อมแสดงเฉลยและคำอธิบายอย่างละเอียดทันที
* **Exam Mode:** โหมดจำลองสอบจริง จับเวลา 90 นาที ไม่แสดงเฉลยระหว่างทำ สรุปคะแนน วิเคราะห์จุดแข็ง-จุดอ่อนแยกตามบท และตรวจดูเฉลยละเอียด
* ผังข้อสอบ (Grid View 1-90) กระโดดข้ามข้อได้ทันที พร้อมระบบปักหมุดข้อที่สงสัย (Flag)

### 4. 🧮 เครื่องคิดเลข IPv4 Subnet Calculator & Quick Ref
* คำนวณ Subnet Mask, Network Address, Broadcast Address, First/Last Usable Host IP, จำนวน Host ทั้งหมด ($2^H$) และ Host ที่ใช้ได้จริง ($2^H - 2$) อัตโนมัติ
* อธิบายวิธีคิดแบบ Block Size ทีละขั้นตอน
* ตารางค่าน้ำหนัก $2^0 - 2^{16}$ และตาราง Subnet Mask Quick Reference

---

## 📁 โครงสร้างโฟลเดอร์ในคลังข้อมูล (Organized Directory Structure)

```text
COM2703-เครือข่าย/
│
├── index.html                   # หน้าเว็บหลัก (Web Portal)
├── styles.css                   # สไตล์ชีท Responsive & Dark/Light Themes
├── app.js                       # ตัวควบคุม Logic เว็บแอปพลิเคชัน
├── .nojekyll                    # ปิดการทำงาน Jekyll บน GitHub Pages
├── README.md                    # เอกสารคู่มือโครงการ
│
├── data/
│   ├── questions90.js           # ฐานข้อมูลข้อสอบ Final 90 ข้อพร้อมเฉลยละเอียด
│   ├── flashcards.js            # ฐานข้อมูลแฟลชการ์ด 65+ คำศัพท์
│   └── summary.js               # เนื้อหาสรุปพร้อมไดอะแกรม SVG คมชัด
│
├── 01_สไลด์บทเรียน/             # รวมสไลด์เลกเชอร์บทเรียน Ch 1 - 8 (PDF)
├── 02_แบบฝึกหัดและการบ้าน/       # รวมแบบฝึกหัด Assignment 1 - 8 และเฉลย (DOCX, PDF)
├── 03_แนวข้อสอบและสรุปทบทวน/    # รวมแนวข้อสอบ Midterm, Final, และข้อสอบเก็บคะแนน (PDF, MD)
├── 04_เอกสารสกัดและสคริปต์/     # ไฟล์ข้อความสกัดและสคริปต์ช่วยประมวลผล
└── quiz_app/                    # เว็บแอปพลิเคชันทบทวน Midterm (100 ข้อ) เดิม
```

---

## 🚀 การติดตั้งและเปิดใช้งาน

1. โคลนคลังข้อมูล:
   ```bash
   git clone https://github.com/cj007zaza/com2703.git
   ```
2. ดับเบิลคลิกเปิดไฟล์ `index.html` บนเบราว์เซอร์ (Chrome, Edge, Safari, Firefox) เพื่อใช้งานได้ทันทีโดยไม่ต้องลงโปรแกรมเสริม
3. หรือเปิดใช้งานผ่าน GitHub Pages: `https://cj007zaza.github.io/com2703/`
