# -*- coding: utf-8 -*-
"""
Generate data/flashcards.js and data/summary.js
"""
import os
import json

base_dir = r"c:\Users\chinj\OneDrive\ปี3\COM2703-เครือข่าย"
data_dir = os.path.join(base_dir, "data")

flashcards = [
    # --- บทที่ 5 ---
    {
        "id": 1,
        "chapter": "บทที่ 5",
        "chapterTitle": "บทที่ 5: โพรโทคอล & OSI Model",
        "term": "PPP (Point-to-Point Protocol)",
        "definition": "โพรโทคอลใน Layer 2 (Data Link) ใช้สื่อสารระหว่างคอมพิวเตอร์ 2 ตัวผ่านการเชื่อมต่อแบบอนุกรม (Serial Interface)",
        "mnemonic": "Layer 2 | จุดต่อจุด 2 เครื่อง | พอร์ต Serial"
    },
    {
        "id": 2,
        "chapter": "บทที่ 5",
        "chapterTitle": "บทที่ 5: โพรโทคอล & OSI Model",
        "term": "ARP (Address Resolution Protocol)",
        "definition": "โพรโทคอลใน Layer 2 ทำหน้าที่แปลงหมายเลขลอจิคัล (IP Address) ให้เป็นหมายเลขฟิสิคัล (MAC Address)",
        "mnemonic": "Layer 2 | แปลง IP -> MAC Address"
    },
    {
        "id": 3,
        "chapter": "บทที่ 5",
        "chapterTitle": "บทที่ 5: โพรโทคอล & OSI Model",
        "term": "RARP (Reverse Address Resolution Protocol)",
        "definition": "โพรโทคอลใน Layer 2 ทำงานตรงข้ามกับ ARP คือแปลงหมายเลข MAC Address ให้เป็น IP Address นิยมใช้กับเครื่อง Diskless Computer",
        "mnemonic": "Layer 2 | แปลง MAC -> IP Address | เครื่องไม่มีฮาร์ดดิสก์"
    },
    {
        "id": 4,
        "chapter": "บทที่ 5",
        "chapterTitle": "บทที่ 5: โพรโทคอล & OSI Model",
        "term": "PPTP (Point-to-Point Tunneling Protocol)",
        "definition": "โพรโทคอลใน Layer 2 ใช้สร้างเครือข่ายเสมือน (VPN) จุดเด่นคือเซ็ตค่าง่าย แต่ระดับความปลอดภัยค่อนข้างต่ำ",
        "mnemonic": "Layer 2 | ทำ VPN | เซ็ตง่าย ปลอดภัยต่ำ"
    },
    {
        "id": 5,
        "chapter": "บทที่ 5",
        "chapterTitle": "บทที่ 5: โพรโทคอล & OSI Model",
        "term": "IP (Internet Protocol)",
        "definition": "โพรโทคอลหลักใน Layer 3 (Network) ทำหน้าที่ระบุที่อยู่ (IP Address) และกำหนดเส้นทางส่งแพ็กเก็ตผ่านเครือข่ายไปยังปลายทาง",
        "mnemonic": "Layer 3 | ระบุที่อยู่แพ็กเก็ต | หาเส้นทาง (Routing)"
    },
    {
        "id": 6,
        "chapter": "บทที่ 5",
        "chapterTitle": "บทที่ 5: โพรโทคอล & OSI Model",
        "term": "ICMP (Internet Control Message Protocol)",
        "definition": "โพรโทคอลใน Layer 3 ใช้ส่งข้อความแจ้งเตือนข้อผิดพลาดและทดสอบสถานะการเชื่อมต่อ เช่น คำสั่ง Ping",
        "mnemonic": "Layer 3 | แจ้งข้อผิดพลาด | คำสั่ง Ping"
    },
    {
        "id": 7,
        "chapter": "บทที่ 5",
        "chapterTitle": "บทที่ 5: โพรโทคอล & OSI Model",
        "term": "IPX / SPX",
        "definition": "ชุดโพรโทคอลของ Novell NetWare: IPX ทำงานใน Layer 3 แบบ Connectionless ส่วน SPX ทำงานใน Layer 4 แบบ Connection-Oriented",
        "mnemonic": "IPX = Layer 3 (Connectionless) | SPX = Layer 4 (Connection-Oriented)"
    },
    {
        "id": 8,
        "chapter": "บทที่ 5",
        "chapterTitle": "บทที่ 5: โพรโทคอล & OSI Model",
        "term": "UDP (User Datagram Protocol)",
        "definition": "โพรโทคอลใน Layer 4 (Transport) ทำงานแบบ Connectionless ไม่มีการตรวจสอบยืนยันการรับส่ง ส่งเร็ว เหมาะกับสตรีมมิ่ง/เกม",
        "mnemonic": "Layer 4 | Connectionless | เร็ว ไม่รอตรวจยืนยัน"
    },
    {
        "id": 9,
        "chapter": "บทที่ 5",
        "chapterTitle": "บทที่ 5: โพรโทคอล & OSI Model",
        "term": "TCP (Transmission Control Protocol)",
        "definition": "โพรโทคอลใน Layer 4 (Transport) ทำงานแบบ Connection-Oriented มีการตรวจสอบยืนยัน (3-way handshake) และควบคุมความถูกต้องแน่นอน",
        "mnemonic": "Layer 4 | Connection-Oriented | ถูกต้องแม่นยำ ยืนยันข้อมูล"
    },
    {
        "id": 10,
        "chapter": "บทที่ 5",
        "chapterTitle": "บทที่ 5: โพรโทคอล & OSI Model",
        "term": "NetBIOS",
        "definition": "โพรโทคอลใน Layer 5 (Session) เป็นตัวกลาง (Interface) ระหว่างระบบปฏิบัติการกับฮาร์ดแวร์ เพื่อให้แอปพลิเคชันสื่อสารผ่านเครือข่ายได้",
        "mnemonic": "Layer 5 | Session Interface ระหว่าง OS กับฮาร์ดแวร์"
    },
    {
        "id": 11,
        "chapter": "บทที่ 5",
        "chapterTitle": "บทที่ 5: โพรโทคอล & OSI Model",
        "term": "SSL (Secure Sockets Layer)",
        "definition": "โพรโทคอลใน Layer 6 (Presentation) ใช้เข้ารหัสข้อมูล (Encryption) ที่รับส่งบนเครือข่าย เช่น เว็บเพจ อีเมล เพื่อความปลอดภัย",
        "mnemonic": "Layer 6 | เข้ารหัสข้อมูล (Encryption) | ปลอดภัย"
    },
    {
        "id": 12,
        "chapter": "บทที่ 5",
        "chapterTitle": "บทที่ 5: โพรโทคอล & OSI Model",
        "term": "DHCP (Dynamic Host Configuration Protocol)",
        "definition": "โพรโทคอลใน Layer 7 (Application) ทำหน้าที่แจกจ่าย IP Address, Subnet Mask และ Gateway ให้เครื่องลูกข่ายอัตโนมัติ",
        "mnemonic": "Layer 7 | แจก IP Address อัตโนมัติ"
    },
    {
        "id": 13,
        "chapter": "บทที่ 5",
        "chapterTitle": "บทที่ 5: โพรโทคอล & OSI Model",
        "term": "FTP (File Transfer Protocol)",
        "definition": "โพรโทคอลใน Layer 7 ใช้สำหรับบริการโอนย้ายแฟ้มข้อมูลระหว่าง Client กับ Server (พอร์ต 20/21)",
        "mnemonic": "Layer 7 | โอนย้ายไฟล์ (Upload/Download)"
    },
    {
        "id": 14,
        "chapter": "บทที่ 5",
        "chapterTitle": "บทที่ 5: โพรโทคอล & OSI Model",
        "term": "FTAM / FAM",
        "definition": "บริการใน Layer 7 สำหรับการเข้าถึง จัดการ และถ่ายโอนไฟล์ข้ามคอมพิวเตอร์ในเครือข่าย เช่น อ่าน เขียน หรือลบไฟล์บนเครื่องอื่น",
        "mnemonic": "Layer 7 | จัดการไฟล์ข้ามเครื่อง อ่าน เขียน ลบ"
    },
    {
        "id": 15,
        "chapter": "บทที่ 5",
        "chapterTitle": "บทที่ 5: โพรโทคอล & OSI Model",
        "term": "HTTP vs HTTPS",
        "definition": "HTTP (พอร์ต 80) เรียกดูเอกสารเว็บ WWW ไม่เข้ารหัส; HTTPS (พอร์ต 443) เรียกดูเว็บ WWW โดยมีการเข้ารหัสข้อมูลผ่าน SSL/TLS ปลอดภัยสูง",
        "mnemonic": "HTTP = พอร์ต 80 ธรรมดา | HTTPS = พอร์ต 443 เข้ารหัสปลอดภัย"
    },
    {
        "id": 16,
        "chapter": "บทที่ 5",
        "chapterTitle": "บทที่ 5: โพรโทคอล & OSI Model",
        "term": "DNS (Domain Name System)",
        "definition": "โพรโทคอลใน Layer 7 ทำหน้าที่แปลงชื่อเว็บไซต์ (Domain Name เช่น google.com) ให้เป็นหมายเลข IP Address (เช่น 142.250.x.x)",
        "mnemonic": "Layer 7 | แปลงชื่อเว็บ (Domain) -> IP Address"
    },
    {
        "id": 17,
        "chapter": "บทที่ 5",
        "chapterTitle": "บทที่ 5: โพรโทคอล & OSI Model",
        "term": "Telnet vs SSH",
        "definition": "Telnet ล็อกอินเครื่องระยะไกลแบบข้อความธรรมดา (พอร์ต 23); SSH ล็อกอินระยะไกลแบบเข้ารหัสข้อมูล ปลอดภัยสูง (พอร์ต 22)",
        "mnemonic": "Telnet = ไม่ปลอดภัย | SSH = พอร์ต 22 เข้ารหัสปลอดภัย"
    },
    {
        "id": 18,
        "chapter": "บทที่ 5",
        "chapterTitle": "บทที่ 5: โพรโทคอล & OSI Model",
        "term": "POP3 vs IMAP",
        "definition": "POP3 รับอีเมลแบบ Offline ดึงเมลลงเครื่องแล้วลบจากเซิร์ฟเวอร์; IMAP รับอีเมลแบบ Online จัดการเมลบนเซิร์ฟเวอร์ ข้อมูลซิงก์ตรงกันทุกอุปกรณ์",
        "mnemonic": "POP3 = Offline ดึงลงเครื่อง | IMAP = Online ซิงก์ทุกอุปกรณ์"
    },
    {
        "id": 19,
        "chapter": "บทที่ 5",
        "chapterTitle": "บทที่ 5: โพรโทคอล & OSI Model",
        "term": "SMTP (Simple Mail Transfer Protocol)",
        "definition": "โพรโทคอลใน Layer 7 ทำหน้าที่ 'ส่งอีเมล' (Send Mail) จากเครื่องผู้ส่งไปยังเซิร์ฟเวอร์ปลายทาง (พอร์ต 25)",
        "mnemonic": "Layer 7 | ส่งอีเมล (Outgoing Mail)"
    },
    {
        "id": 20,
        "chapter": "บทที่ 5",
        "chapterTitle": "บทที่ 5: โพรโทคอล & OSI Model",
        "term": "MQTT (Message Queue Telemetry Transport)",
        "definition": "โพรโทคอลขนาดเล็กน้ำหนักเบา ออกแบบสำหรับการสื่อสารระหว่างเครื่องต่อเครื่อง (M2M) และระบบ Internet of Things (IoT) แบบ Real-Time",
        "mnemonic": "Layer 7 | IoT & M2M | ข้อมูลเล็ก Real-time ประหยัดพลังงาน"
    },

    # --- บทที่ 6 ---
    {
        "id": 21,
        "chapter": "บทที่ 6",
        "chapterTitle": "บทที่ 6: ระบบเครือข่าย & Routing",
        "term": "PAN (Personal Area Network)",
        "definition": "เครือข่ายส่วนบุคคล มีรัศมีการสื่อสารระยะสั้นไม่เกิน 10 เมตร เช่น Hotspot มือถือ, Bluetooth",
        "mnemonic": "ระยะทาง <= 10 เมตร | ส่วนบุคคล Hotspot/Bluetooth"
    },
    {
        "id": 22,
        "chapter": "บทที่ 6",
        "chapterTitle": "บทที่ 6: ระบบเครือข่าย & Routing",
        "term": "LAN (Local Area Network)",
        "definition": "เครือข่ายท้องถิ่นหรือเฉพาะบริเวณ ครอบคลุมพื้นที่ขนาดเล็ก เช่น ในห้อง หรือในอาคารเดียวกัน ระยะทางไม่เกิน 10 กิโลเมตร",
        "mnemonic": "ระยะทาง <= 10 กม. | ในห้อง ตึก อาคารเดียวกัน"
    },
    {
        "id": 23,
        "chapter": "บทที่ 6",
        "chapterTitle": "บทที่ 6: ระบบเครือข่าย & Routing",
        "term": "MAN (Metropolitan Area Network)",
        "definition": "เครือข่ายระดับเมืองหรือนครหลวง ครอบคลุมพื้นที่กว้างกว่า LAN แต่แคบกว่า WAN เช่น เครือข่ายเคเบิลทีวีเมือง",
        "mnemonic": "ระดับเมือง/เทศบาล | กว้างกว่า LAN แคบกว่า WAN"
    },
    {
        "id": 24,
        "chapter": "บทที่ 6",
        "chapterTitle": "บทที่ 6: ระบบเครือข่าย & Routing",
        "term": "WAN (Wide Area Network)",
        "definition": "เครือข่ายวงกว้าง ครอบคลุมระดับจังหวัด ประเทศ หรือทั่วโลก มักใช้สายวงจรเช่า (Leased Line) และดาวเทียม",
        "mnemonic": "ระดับจังหวัด ประเทศ โลก | สายวงจรเช่า (Leased Line)"
    },
    {
        "id": 25,
        "chapter": "บทที่ 6",
        "chapterTitle": "บทที่ 6: ระบบเครือข่าย & Routing",
        "term": "Circuit-Switching",
        "definition": "ระบบสลับวงจรที่ต้องจับจองวงจรสื่อสารตลอดเส้นทางไว้ตลอดเวลา ผู้อื่นไม่สามารถแทรกได้ เช่น เครือข่ายโทรศัพท์พื้นฐาน",
        "mnemonic": "จองสายตลอดเวลา | คนอื่นใช้ไม่ได้ | เหมือนโทรศัพท์"
    },
    {
        "id": 26,
        "chapter": "บทที่ 6",
        "chapterTitle": "บทที่ 6: ระบบเครือข่าย & Routing",
        "term": "Message-Switching (Store and Forward)",
        "definition": "ส่งข้อมูลโดยไม่ต้องจองวงจรล่วงหน้า โหนดจะเก็บข้อมูลไว้จนกว่าโหนดถัดไปจะพร้อมรับแล้วจึงส่งต่อ (Store and Forward)",
        "mnemonic": "ไม่จองสายล่วงหน้า | เก็บแล้วส่งต่อ (Store and Forward)"
    },
    {
        "id": 27,
        "chapter": "บทที่ 6",
        "chapterTitle": "บทที่ 6: ระบบเครือข่าย & Routing",
        "term": "Packet-Switching",
        "definition": "ซอยข้อมูลออกเป็นชิ้นเล็กๆ ขนาดเท่ากันเรียกว่า Packet แล้วส่งผ่านโครงข่าย มี 3 รูปแบบ: Datagram, SVC, PVC",
        "mnemonic": "แบ่งข้อมูลเป็น Packet เท่าๆ กัน | มี Datagram, SVC, PVC"
    },
    {
        "id": 28,
        "chapter": "บทที่ 6",
        "chapterTitle": "บทที่ 6: ระบบเครือข่าย & Routing",
        "term": "Datagram Service",
        "definition": "การส่งแพ็กเกตที่แต่ละแพ็กเกตเป็นอิสระต่อกัน ไปคนละเส้นทางได้ ถึงปลายทางสลับลำดับกันได้ เหมาะกับข้อมูลสั้นๆ",
        "mnemonic": "แพ็กเกตอิสระ | คนละเส้นทาง | เหมาะกับข้อมูลสั้นๆ"
    },
    {
        "id": 29,
        "chapter": "บทที่ 6",
        "chapterTitle": "บทที่ 6: ระบบเครือข่าย & Routing",
        "term": "SVC (Switched Virtual Circuit)",
        "definition": "วงจรเสมือนที่สร้างขึ้นชั่วคราวเมื่อต้องการส่งข้อมูล และยกเลิกเมื่อส่งเสร็จ ไม่บล็อกผู้อื่น เหมาะกับข้อมูลปริมาณมาก",
        "mnemonic": "วงจรเสมือนชั่วคราว | ไม่บล็อกคนอื่น | ข้อมูลปริมาณมาก"
    },
    {
        "id": 30,
        "chapter": "บทที่ 6",
        "chapterTitle": "บทที่ 6: ระบบเครือข่าย & Routing",
        "term": "PVC (Permanent Virtual Circuit)",
        "definition": "วงจรเสมือนที่กำหนดไว้อย่างถาวรเหมือนสายเช่า (Leased Line) เหมาะกับการส่งข้อมูลเป็นประจำและมีปริมาณมาก",
        "mnemonic": "วงจรเสมือนถาวร | เหมือนสายเช่า | ข้อมูลมากและเป็นประจำ"
    },
    {
        "id": 31,
        "chapter": "บทที่ 6",
        "chapterTitle": "บทที่ 6: ระบบเครือข่าย & Routing",
        "term": "Centralized Routing",
        "definition": "การหาเส้นทางโดยมีโหนดศูนย์กลางเป็นผู้ตัดสินใจเลือกเส้นทาง ข้อเสีย: ถ้าศูนย์กลางล่ม ระบบหาเส้นทางจะล่มทั้งหมด",
        "mnemonic": "ศูนย์กลางเลือกเส้นทาง | ข้อเสีย: จุดศูนย์กลางล่มระบบพัง"
    },
    {
        "id": 32,
        "chapter": "บทที่ 6",
        "chapterTitle": "บทที่ 6: ระบบเครือข่าย & Routing",
        "term": "Static Routing",
        "definition": "การหาเส้นทางแบบสถิตย์ ใช้เส้นทางเดิมตายตัวเสมอ ข้อเสีย: ถ้าเส้นทางชำรุด จะส่งข้อมูลไม่ได้ ต้องรอผู้ดูแลมาแก้",
        "mnemonic": "เส้นทางเดิมตายตัว | ข้อเสีย: สายขาดส่งไม่ผ่าน"
    },
    {
        "id": 33,
        "chapter": "บทที่ 6",
        "chapterTitle": "บทที่ 6: ระบบเครือข่าย & Routing",
        "term": "Dynamic / Adaptive Routing",
        "definition": "การหาเส้นทางแบบพลวัต เปลี่ยนเส้นทางอัตโนมัติตามสภาพสาย เลี่ยงเส้นทางเสีย ข้อเสีย: เสียเวลาคำนวณหาเส้นทางใหม่ทุกครั้ง",
        "mnemonic": "เปลี่ยนเส้นทางอัตโนมัติ | ข้อเสีย: เสียเวลาคำนวณก่อนส่ง"
    },
    {
        "id": 34,
        "chapter": "บทที่ 6",
        "chapterTitle": "บทที่ 6: ระบบเครือข่าย & Routing",
        "term": "Flooding / Broadcast Routing",
        "definition": "การค้นหาเส้นทางโดยส่งข้อมูลกระจายไปยังทุกโหนด ข้อเสีย: ทำให้เกิดข้อมูลซ้ำซ้อนและสิ้นเปลืองแบนด์วิดท์",
        "mnemonic": "ส่งกระจายทุกโหนด | ข้อเสีย: ข้อมูลซ้ำซ้อน เปลืองเน็ต"
    },
    {
        "id": 35,
        "chapter": "บทที่ 6",
        "chapterTitle": "บทที่ 6: ระบบเครือข่าย & Routing",
        "term": "Distributed Systems: 4 มิติ",
        "definition": "ระบบกระจายศูนย์แบ่งได้ 4 มิติ: 1) ตามตำแหน่ง (Location) 2) ตามหน้าที่งาน (Functions เช่น บัญชี) 3) ตามการควบคุม (Control) 4) ตามการประมวลผล (Hierarchical vs Horizontal)",
        "mnemonic": "ตำแหน่ง | หน้าที่ | ควบคุม | ประมวลผล (ลำดับชั้น / ระนาบ)"
    },

    # --- บทที่ 7 ---
    {
        "id": 36,
        "chapter": "บทที่ 7",
        "chapterTitle": "บทที่ 7: ระบบเครือข่าย LAN & Topology",
        "term": "BUS Topology",
        "definition": "ใช้สายแกนร่วมเส้นเดียว มี Terminator ที่ปลายสองข้างป้องกันสัญญาณสะท้อนกลับ ข้อดี: ราคาถูก ใช้สายน้อย ข้อเสีย: สายหลักขาดพังทั้งระบบ",
        "mnemonic": "สายเดี่ยว | มี Terminator กัน Echo | ถูก ใช้สายน้อย | สายขาดพังหมด"
    },
    {
        "id": 37,
        "chapter": "บทที่ 7",
        "chapterTitle": "บทที่ 7: ระบบเครือข่าย LAN & Topology",
        "term": "RING Topology",
        "definition": "เชื่อมต่อเป็นวงกลม ส่งข้อมูลทางเดียว ข้อดี: ใช้สายน้อย ข้อมูลไม่ชนกัน ข้อเสีย: โหนดใดเสียพังทั้งระบบ เพิ่มเครื่องยากต้องหยุดทั้งวง",
        "mnemonic": "วงกลมทิศทางเดียว | ไม่ชนกัน | โหนดเสียพังทั้งวง เพิ่มเครื่องยาก"
    },
    {
        "id": 38,
        "chapter": "บทที่ 7",
        "chapterTitle": "บทที่ 7: ระบบเครือข่าย LAN & Topology",
        "term": "STAR Topology",
        "definition": "มีจุดศูนย์กลางคือ Hub หรือ Switch ข้อดี: ติดตั้งง่าย สายขาดเส้นหนึ่งจุดอื่นยังทำงานได้ ข้อเสีย: แพง ใช้สายมาก ถ้า Hub/Switch พัง ล่มทั้งระบบ",
        "mnemonic": "ศูนย์กลาง Hub/Switch | สายนอกขาดไม่กระทบอื่น | ศูนย์กลางพังล่มหมด"
    },
    {
        "id": 39,
        "chapter": "บทที่ 7",
        "chapterTitle": "บทที่ 7: ระบบเครือข่าย LAN & Topology",
        "term": "STAR-wire RING & MAU",
        "definition": "นำ Star และ Ring มารวมกัน สายโยงเข้ากล่อง MAU (Multistation Access Unit) ควบคุมวงแหวนภายใน สามารถตัดวงจรโหนดที่เสียแบบ Bypass ได้",
        "mnemonic": "รวม Star + Ring | กล่อง MAU ตัดโหนดเสียแบบ Bypass"
    },
    {
        "id": 40,
        "chapter": "บทที่ 7",
        "chapterTitle": "บทที่ 7: ระบบเครือข่าย LAN & Topology",
        "term": "MESH Topology",
        "definition": "เชื่อมต่อทุกโหนดแบบจุดต่อจุดสมบูรณ์ (Point-to-Point) ข้อดี: ปลอดภัยสูง สายชำรุดระบบยังทำงานได้ ข้อเสีย: ใช้สายสัญญาณมากที่สุดและแพงที่สุด",
        "mnemonic": "จุดต่อจุดครบทุกคู่ | ปลอดภัยสูงมาก | เปลืองสายและแพงที่สุด"
    },
    {
        "id": 41,
        "chapter": "บทที่ 7",
        "chapterTitle": "บทที่ 7: ระบบเครือข่าย LAN & Topology",
        "term": "FDDI (Fiber Distributed Data Interface)",
        "definition": "เครือข่ายวงแหวนคู่สายใยแก้วนำแสง (Dual Ring) ส่งข้อมูลสวนทางกัน เร็วและทนทานสูง นิยมใช้ทำเครือข่ายแกนหลัก (Backbone)",
        "mnemonic": "วงแหวนคู่ Fiber | หมุนสวนทางกัน | ทำ Backbone ความเร็วสูง"
    },
    {
        "id": 42,
        "chapter": "บทที่ 7",
        "chapterTitle": "บทที่ 7: ระบบเครือข่าย LAN & Topology",
        "term": "File Server vs Disk Server",
        "definition": "File Server จัดการการจัดเก็บและแชร์แฟ้มข้อมูล ส่วน Disk Server ควบคุมและจัดสรรโควตาพื้นที่บนฮาร์ดดิสก์ให้ผู้ใช้",
        "mnemonic": "File Server = แชร์ไฟล์ | Disk Server = จัดสรรโควตาฮาร์ดดิสก์"
    },
    {
        "id": 43,
        "chapter": "บทที่ 7",
        "chapterTitle": "บทที่ 7: ระบบเครือข่าย LAN & Topology",
        "term": "Proxy Server & Web Cache",
        "definition": "เซิร์ฟเวอร์ที่ทำหน้าที่เก็บแคชหน้าเว็บที่เคยเปิดไว้ ช่วยลดปริมาณ Data-stream ในเครือข่ายและประหยัดแบนด์วิดท์",
        "mnemonic": "แคชหน้าเว็บ | ลด Data-stream | เปิดเว็บเร็วขึ้น"
    },
    {
        "id": 44,
        "chapter": "บทที่ 7",
        "chapterTitle": "บทที่ 7: ระบบเครือข่าย LAN & Topology",
        "term": "Point-to-Point vs Multidrop",
        "definition": "Point-to-Point เชื่อม 2 เครื่อง จับจองช่องทาง 100% เร็วเต็มที่; Multidrop เชื่อมหลายเครื่องแชร์สายเส้นเดียว ประหยัดสายแต่อาจชนกัน",
        "mnemonic": "Point-to-Point = 2 เครื่องเต็มสปีด | Multidrop = แชร์สายหลายเครื่อง"
    },
    {
        "id": 45,
        "chapter": "บทที่ 7",
        "chapterTitle": "บทที่ 7: ระบบเครือข่าย LAN & Topology",
        "term": "Ethernet Standards (อีเทอร์เน็ต)",
        "definition": "10Base2 (Thin Coax 185m), 10Base5 (Thick Coax 500m), 10BaseT (UTP 10Mbps), 100BaseTX (Fast Ethernet 100Mbps), 1000BaseT (Gigabit Ethernet 1Gbps)",
        "mnemonic": "ตัวเลข = สปีด (Mbps) | Base = Baseband | ท้าย = สื่อ (T=UTP, F=Fiber)"
    },
    {
        "id": 46,
        "chapter": "บทที่ 7",
        "chapterTitle": "บทที่ 7: ระบบเครือข่าย LAN & Topology",
        "term": "อุปกรณ์เครือข่ายตามชั้น OSI",
        "definition": "Layer 1: Repeater (ทวนสัญญาณ), Hub | Layer 2: Bridge, Switch (คัดกรองตาม MAC) | Layer 3: Router (ตาม IP) | สูงกว่า: Gateway (แปลงโพรโทคอล)",
        "mnemonic": "L1: Hub/Repeater | L2: Switch/Bridge | L3: Router | All: Gateway"
    },

    # --- บทที่ 8 ---
    {
        "id": 47,
        "chapter": "บทที่ 8",
        "chapterTitle": "บทที่ 8: Subnetting & IP Addressing",
        "term": "IPv4 vs IPv6 (ขนาดและจำนวน)",
        "definition": "IPv4 มี 32 บิต (4 Octets) รองรับได้ 2^32 หมายเลข; IPv6 มี 128 บิต (8 Hextets) รองรับได้ 2^128 หมายเลข",
        "mnemonic": "IPv4 = 32 บิต (2^32) | IPv6 = 128 บิต (2^128)"
    },
    {
        "id": 48,
        "chapter": "บทที่ 8",
        "chapterTitle": "บทที่ 8: Subnetting & IP Addressing",
        "term": "IPv6 Zero Compression กฎการย่อ",
        "definition": "1) ตัดเลขศูนย์นำหน้าได้ (เช่น :00A9: -> :A9:) 2) ย่อกลุ่มที่เป็น 0000 ติดกันเป็น :: ได้ 'ครั้งเดียวเท่านั้น' ในหนึ่งที่อยู่",
        "mnemonic": "ตัด 0 นำหน้าได้ | ย่อกลุ่ม 0 เป็น :: ได้แค่ 1 ครั้งเท่านั้น!"
    },
    {
        "id": 49,
        "chapter": "บทที่ 8",
        "chapterTitle": "บทที่ 8: Subnetting & IP Addressing",
        "term": "Class A (IPv4)",
        "definition": "Octet แรก 0 - 127, NetID 8 บิต (ใช้จริง 7 บิต), HostID 24 บิต, Default Mask: 255.0.0.0, โฮสต์ต่อเครือข่าย 2^24 - 2 (16 ล้านโฮสต์)",
        "mnemonic": "Class A: 0 - 127 | NetID 8 บิต | HostID 24 บิต | Mask 255.0.0.0"
    },
    {
        "id": 50,
        "chapter": "บทที่ 8",
        "chapterTitle": "บทที่ 8: Subnetting & IP Addressing",
        "term": "Class B (IPv4)",
        "definition": "Octet แรก 128 - 191, NetID 16 บิต (ใช้จริง 14 บิต), HostID 16 บิต, Default Mask: 255.255.0.0, โฮสต์ต่อเครือข่าย 2^16 - 2 (65,534 โฮสต์)",
        "mnemonic": "Class B: 128 - 191 | NetID 16 บิต | HostID 16 บิต | Mask 255.255.0.0"
    },
    {
        "id": 51,
        "chapter": "บทที่ 8",
        "chapterTitle": "บทที่ 8: Subnetting & IP Addressing",
        "term": "Class C (IPv4)",
        "definition": "Octet แรก 192 - 223, NetID 24 บิต (ใช้จริง 21 บิต), HostID 8 บิต, Default Mask: 255.255.255.0, โฮสต์ต่อเครือข่าย 2^8 - 2 = 254 โฮสต์",
        "mnemonic": "Class C: 192 - 223 | NetID 24 บิต | HostID 8 บิต | Mask 255.255.255.0"
    },
    {
        "id": 52,
        "chapter": "บทที่ 8",
        "chapterTitle": "บทที่ 8: Subnetting & IP Addressing",
        "term": "Class D & Class E",
        "definition": "Class D (224 - 239) ใช้สำหรับ Multicast (ส่งกลุ่มเฉพาะ); Class E (240 - 255) สำรองไว้เพื่อการทดลองในอนาคต (Reserved)",
        "mnemonic": "Class D: 224 - 239 (Multicast) | Class E: 240 - 255 (สำรองทดลอง)"
    },
    {
        "id": 53,
        "chapter": "บทที่ 8",
        "chapterTitle": "บทที่ 8: Subnetting & IP Addressing",
        "term": "การแยก NetID และ HostID",
        "definition": "Class A: NetID 1 ส่วน, HostID 3 ส่วน (เช่น 10.6.5.42 -> NetID=10, HostID=6.5.42); Class B: 2 ส่วน/2 ส่วน; Class C: 3 ส่วน/1 ส่วน",
        "mnemonic": "ดู Octet แรกบอก Class -> A=1 ส่วน, B=2 ส่วน, C=3 ส่วน สำหรับ NetID"
    },
    {
        "id": 54,
        "chapter": "บทที่ 8",
        "chapterTitle": "บทที่ 8: Subnetting & IP Addressing",
        "term": "ค่าน้ำหนัก 8 บิต (Magic Bit Weights)",
        "definition": "128, 64, 32, 16, 8, 4, 2, 1 | ค่า Subnet Mask สะสม: 1บิต=128, 2บิต=192, 3บิต=224, 4บิต=240, 5บิต=248, 6บิต=252, 7บิต=254, 8บิต=255",
        "mnemonic": "128 | 192 | 224 | 240 | 248 | 252 | 254 | 255 (ต้องจำให้ขึ้นใจ!)"
    },
    {
        "id": 55,
        "chapter": "บทที่ 8",
        "chapterTitle": "บทที่ 8: Subnetting & IP Addressing",
        "term": "สูตรคำนวณ Subnet & Host",
        "definition": "จำนวน Subnet = 2^N (N = บิตที่ยืมมา) | จำนวน Host ต่อ Subnet = 2^H (H = บิต 0 ที่เหลือ) | Host ที่ใช้ได้จริง = 2^H - 2 (หัก Network IP และ Broadcast IP)",
        "mnemonic": "Subnet = 2^N | Host ทั้งหมด = 2^H | Host ใช้งานได้ = 2^H - 2"
    },
    {
        "id": 56,
        "chapter": "บทที่ 8",
        "chapterTitle": "บทที่ 8: Subnetting & IP Addressing",
        "term": "Network Address vs Broadcast Address",
        "definition": "Network Address คือหมายเลขแรกสุดของซับเน็ต (บิตโฮสต์เป็น 0 ทั้งหมด); Broadcast Address คือหมายเลขท้ายสุดของซับเน็ต (บิตโฮสต์เป็น 1 ทั้งหมด) ทั้งสองตัวห้ามตั้งให้ Host",
        "mnemonic": "Network = ตัวแรกสุด (.0) | Broadcast = ตัวท้ายสุด (.255)"
    },
    {
        "id": 57,
        "chapter": "บทที่ 8",
        "chapterTitle": "บทที่ 8: Subnetting & IP Addressing",
        "term": "เทคนิค Block Size (ระยะก้าวซับเน็ต)",
        "definition": "Block Size = 256 - ค่า Mask ใน Octet นั้น (หรือ 2^H ใน Octet นั้น) Network Address ใน Octet นั้นจะเป็นพหุคูณของ Block Size ที่ไม่เกินค่า IP",
        "mnemonic": "Block Size = 256 - Mask | Network Address = พหุคูณที่ไม่เกิน IP"
    },
    {
        "id": 58,
        "chapter": "บทที่ 8",
        "chapterTitle": "บทที่ 8: Subnetting & IP Addressing",
        "term": "CIDR /30 (Point-to-Point Link)",
        "definition": "Mask คือ 255.255.255.252 บิตโฮสต์เหลือ 2 บิต จำนวนโฮสต์ที่ใช้ได้จริง = 2^2 - 2 = 2 โฮสต์ นิยมใช้เชื่อมต่อระหว่าง Router 2 ตัว",
        "mnemonic": "/30 = 255.255.255.252 | โฮสต์ใช้ได้จริง 2 ตัว (สำหรับ Router-to-Router)"
    },
    {
        "id": 59,
        "chapter": "บทที่ 8",
        "chapterTitle": "บทที่ 8: Subnetting & IP Addressing",
        "term": "CIDR /28 (14 Usable Hosts)",
        "definition": "Mask คือ 255.255.255.240 บิตโฮสต์เหลือ 4 บิต Block size = 16 จำนวนโฮสต์ที่ใช้ได้จริง = 2^4 - 2 = 14 โฮสต์",
        "mnemonic": "/28 = 255.255.255.240 | Block size 16 | โฮสต์ใช้ได้ 14 ตัว"
    },
    {
        "id": 60,
        "chapter": "บทที่ 8",
        "chapterTitle": "บทที่ 8: Subnetting & IP Addressing",
        "term": "การหา Subnet Mask จากจำนวน IP ที่ต้องการ",
        "definition": "หา 2^H >= จำนวน IP ที่ต้องการ เช่น ต้องการ 2,000 IP -> 2^11 = 2,048 -> H=11 บิต -> Mask มีบิต 1 เท่ากับ 32-11 = 21 บิต -> 255.255.248.0",
        "mnemonic": "2^7=128, 2^8=256, 2^9=512, 2^10=1024, 2^11=2048 (หาค่า 2^H ที่คลุม)"
    },
    {
        "id": 61,
        "chapter": "บทที่ 8",
        "chapterTitle": "บทที่ 8: Subnetting & IP Addressing",
        "term": "IP 10.10.10.0/13 เซ็ตให้ Host ได้หรือไม่?",
        "definition": "ได้! เพราะ /13 มีช่วง Network คือ 10.8.0.0 และ Broadcast คือ 10.15.255.255 ทำให้ 10.10.10.0 ตกอยู่ในช่วงโฮสต์ใช้งานได้พอดี อย่าหลงกลเลข .0",
        "mnemonic": "เซ็ตให้โฮสต์ได้! เพราะไม่ใช่ Network IP หรือ Broadcast IP ของซับเน็ตนี้"
    },
    {
        "id": 62,
        "chapter": "บทที่ 8",
        "chapterTitle": "บทที่ 8: Subnetting & IP Addressing",
        "term": "สัญลักษณ์ Cisco Packet Tracer: Router",
        "definition": "รูปทรงกระบอกกลม มีลูกศร 4 ทิศทางวิ่งเข้าหากันและชี้ออก ทำหน้าที่หาเส้นทางและส่งต่อข้อมูลใน Layer 3",
        "mnemonic": "ทรงกระบอกกลม + ลูกศร 4 ทิศทาง = Router"
    },
    {
        "id": 63,
        "chapter": "บทที่ 8",
        "chapterTitle": "บทที่ 8: Subnetting & IP Addressing",
        "term": "สัญลักษณ์ Cisco Packet Tracer: Switch",
        "definition": "รูปกล่องสี่เหลี่ยม มีลูกศร 4 เส้นวิ่งสวนทางกันซ้าย-ขวา ทำหน้าที่สลับสายและส่งข้อมูลในระดับ Layer 2",
        "mnemonic": "กล่องสี่เหลี่ยม + ลูกศรสวนทางกัน 4 เส้น = Switch"
    },
    {
        "id": 64,
        "chapter": "บทที่ 8",
        "chapterTitle": "บทที่ 8: Subnetting & IP Addressing",
        "term": "สัญลักษณ์ Cisco Packet Tracer: Hub",
        "definition": "รูปกล่องสี่เหลี่ยม มีลูกศรเส้นเดียวชี้กระจายออกทุกทิศทาง ทำหน้าที่กระจายสัญญาณใน Layer 1",
        "mnemonic": "กล่องสี่เหลี่ยม + ลูกศรกระจายออกทุกทาง = Hub"
    },
    {
        "id": 65,
        "chapter": "บทที่ 8",
        "chapterTitle": "บทที่ 8: Subnetting & IP Addressing",
        "term": "สัญลักษณ์ Cisco Packet Tracer: Cloud",
        "definition": "รูปก้อนเมฆ (Network Cloud) เป็นตัวแทนของเครือข่ายภายนอกวงกว้าง เช่น WAN, Frame Relay หรือ Internet",
        "mnemonic": "รูปก้อนเมฆ = เครือข่ายภายนอก WAN / Internet"
    }
]

# Write to data/flashcards.js
flashcards_path = os.path.join(data_dir, "flashcards.js")
with open(flashcards_path, "w", encoding="utf-8") as f:
    f.write("// Flashcards Dataset for COM2703 (Chapters 5-8)\n")
    f.write("window.FLASHCARDS_DATA = ")
    json.dump(flashcards, f, ensure_ascii=False, indent=2)
    f.write(";\n")

print(f"Generated data/flashcards.js successfully ({len(flashcards)} flashcards)!")
