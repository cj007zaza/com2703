# -*- coding: utf-8 -*-
"""
Generate data/summary.js containing comprehensive illustrated study guides
with high quality responsive SVG diagrams and tables for Chapters 5-8.
"""
import os
import json

base_dir = r"c:\Users\chinj\OneDrive\ปี3\COM2703-เครือข่าย"
data_dir = os.path.join(base_dir, "data")

summary_data = {
    "ch5": {
        "title": "บทที่ 5: โพรโทคอล & OSI Model (Protocols & OSI Architecture)",
        "badge": "บทที่ 5",
        "description": "เจาะลึกโพรโทคอลสื่อสาร การจับคู่ Layer ในแบบจำลอง OSI 7 ชั้น และหน้าที่สำคัญที่ออกสอบ",
        "content_html": """
        <div class="summary-card">
            <h3>📌 1. โครงสร้างแบบจำลอง OSI Model 7 ชั้น และการจับคู่ Protocol</h3>
            <p>แบบจำลอง OSI (Open Systems Interconnection) แบ่งการสื่อสารออกเป็น 7 เลเยอร์ โดยข้อสอบมักถามว่า <strong>"โพรโทคอลนี้ทำงานใน Layer ใด?"</strong></p>
            
            <div class="diagram-box">
                <div class="diagram-title">🎨 แผนผัง OSI 7-Layer Protocol Map</div>
                <div class="svg-wrapper">
                    <svg viewBox="0 0 750 480" width="100%" height="auto" class="responsive-svg">
                        <defs>
                            <linearGradient id="grad7" x1="0%" y1="0%" x2="100%" y2="0%">
                                <stop offset="0%" stop-color="#4f46e5"/><stop offset="100%" stop-color="#7c3aed"/>
                            </linearGradient>
                            <linearGradient id="grad6" x1="0%" y1="0%" x2="100%" y2="0%">
                                <stop offset="0%" stop-color="#0284c7"/><stop offset="100%" stop-color="#2563eb"/>
                            </linearGradient>
                            <linearGradient id="grad5" x1="0%" y1="0%" x2="100%" y2="0%">
                                <stop offset="0%" stop-color="#0d9488"/><stop offset="100%" stop-color="#0284c7"/>
                            </linearGradient>
                            <linearGradient id="grad4" x1="0%" y1="0%" x2="100%" y2="0%">
                                <stop offset="0%" stop-color="#16a34a"/><stop offset="100%" stop-color="#059669"/>
                            </linearGradient>
                            <linearGradient id="grad3" x1="0%" y1="0%" x2="100%" y2="0%">
                                <stop offset="0%" stop-color="#d97706"/><stop offset="100%" stop-color="#b45309"/>
                            </linearGradient>
                            <linearGradient id="grad2" x1="0%" y1="0%" x2="100%" y2="0%">
                                <stop offset="0%" stop-color="#ea580c"/><stop offset="100%" stop-color="#c2410c"/>
                            </linearGradient>
                            <linearGradient id="grad1" x1="0%" y1="0%" x2="100%" y2="0%">
                                <stop offset="0%" stop-color="#dc2626"/><stop offset="100%" stop-color="#991b1b"/>
                            </linearGradient>
                        </defs>
                        <!-- Layer 7 -->
                        <rect x="20" y="20" width="710" height="52" rx="10" fill="url(#grad7)"/>
                        <text x="40" y="52" fill="#ffffff" font-size="16" font-weight="bold">Layer 7: Application</text>
                        <text x="240" y="52" fill="#f8fafc" font-size="14">HTTP(80), HTTPS(443), FTP(20/21), DNS, DHCP, Telnet, SSH(22), POP3, IMAP, SMTP(25), MQTT</text>
                        <!-- Layer 6 -->
                        <rect x="20" y="82" width="710" height="52" rx="10" fill="url(#grad6)"/>
                        <text x="40" y="114" fill="#ffffff" font-size="16" font-weight="bold">Layer 6: Presentation</text>
                        <text x="240" y="114" fill="#f8fafc" font-size="14">SSL (Secure Sockets Layer), TLS, การเข้ารหัสข้อมูล (Encryption), การบีบอัดข้อมูล</text>
                        <!-- Layer 5 -->
                        <rect x="20" y="144" width="710" height="52" rx="10" fill="url(#grad5)"/>
                        <text x="40" y="176" fill="#ffffff" font-size="16" font-weight="bold">Layer 5: Session</text>
                        <text x="240" y="176" fill="#f8fafc" font-size="14">NetBIOS (Network Basic Input/Output System) เชื่อมต่อ OS กับฮาร์ดแวร์เพื่อรันแอป</text>
                        <!-- Layer 4 -->
                        <rect x="20" y="206" width="710" height="52" rx="10" fill="url(#grad4)"/>
                        <text x="40" y="238" fill="#ffffff" font-size="16" font-weight="bold">Layer 4: Transport</text>
                        <text x="240" y="238" fill="#f8fafc" font-size="14">TCP (Connection-Oriented ตรวจสอบยืนยัน), UDP (Connectionless รวดเร็ว), SPX</text>
                        <!-- Layer 3 -->
                        <rect x="20" y="268" width="710" height="52" rx="10" fill="url(#grad3)"/>
                        <text x="40" y="300" fill="#ffffff" font-size="16" font-weight="bold">Layer 3: Network</text>
                        <text x="240" y="300" fill="#f8fafc" font-size="14">IP (IPv4/IPv6), ICMP (คำสั่ง Ping/แจ้งข้อผิดพลาด), IPX, ค้นหาเส้นทาง (Router)</text>
                        <!-- Layer 2 -->
                        <rect x="20" y="330" width="710" height="52" rx="10" fill="url(#grad2)"/>
                        <text x="40" y="362" fill="#ffffff" font-size="16" font-weight="bold">Layer 2: Data Link</text>
                        <text x="240" y="362" fill="#f8fafc" font-size="14">PPP (สาย Serial), ARP (IP->MAC), RARP (MAC->IP สำหรับ Diskless), PPTP (VPN), Switch/Bridge</text>
                        <!-- Layer 1 -->
                        <rect x="20" y="392" width="710" height="52" rx="10" fill="url(#grad1)"/>
                        <text x="40" y="424" fill="#ffffff" font-size="16" font-weight="bold">Layer 1: Physical</text>
                        <text x="240" y="424" fill="#f8fafc" font-size="14">สายสัญญาณ (UTP, Coax, Fiber Optic), สัญญาณไฟฟ้า/คลื่นวิทยุ, Repeater, Hub</text>
                    </svg>
                </div>
            </div>

            <h3>📌 2. เปรียบเทียบโพรโทคอลคู่เหมือนที่ข้อสอบชอบถามสลับกัน</h3>
            <div class="comparison-grid">
                <div class="comp-card">
                    <div class="comp-header primary">ARP vs RARP (Layer 2)</div>
                    <ul>
                        <li><strong>ARP:</strong> แปลง <code>IP Address $\rightarrow$ MAC Address</code></li>
                        <li><strong>RARP:</strong> แปลง <code>MAC Address $\rightarrow$ IP Address</code> (สำหรับเครื่อง Diskless Computer ไม่มีฮาร์ดดิสก์)</li>
                    </ul>
                </div>
                <div class="comp-card">
                    <div class="comp-header success">TCP vs UDP (Layer 4)</div>
                    <ul>
                        <li><strong>TCP:</strong> <code>Connection-Oriented</code> มีการตรวจสอบยืนยัน (Ack) น่าเชื่อถือสูง</li>
                        <li><strong>UDP:</strong> <code>Connectionless</code> ไม่ตรวจสอบยืนยัน รวดเร็วมาก เหมาะกับ Streaming/Gaming/VoIP</li>
                    </ul>
                </div>
                <div class="comp-card">
                    <div class="comp-header warning">POP3 vs IMAP (Layer 7 Email)</div>
                    <ul>
                        <li><strong>POP3:</strong> <code>Offline</code> ดาวน์โหลดอีเมลลงเครื่องแล้วลบจากเซิร์ฟเวอร์</li>
                        <li><strong>IMAP:</strong> <code>Online</code> จัดการอีเมลบนเซิร์ฟเวอร์ ซิงก์ตรงกันทุกอุปกรณ์</li>
                        <li><strong>SMTP:</strong> ใช้สำหรับ <strong>ส่งอีเมล (Outgoing)</strong></li>
                    </ul>
                </div>
                <div class="comp-card">
                    <div class="comp-header info">Telnet vs SSH & MQTT</div>
                    <ul>
                        <li><strong>Telnet (พอร์ต 23):</strong> Remote Login แบบข้อความธรรมดา (ไม่ปลอดภัย)</li>
                        <li><strong>SSH (พอร์ต 22):</strong> Remote Access แบบเข้ารหัสข้อมูล (ปลอดภัยสูง)</li>
                        <li><strong>MQTT:</strong> โพรโทคอลสำหรับ <code>M2M</code> และ <code>IoT</code> ส่ง Real-Time ประหยัดแบนด์วิดท์</li>
                    </ul>
                </div>
            </div>
        </div>
        """
    },
    "ch6": {
        "title": "บทที่ 6: ระบบเครือข่าย & Routing (Network Architectures & Switching)",
        "badge": "บทที่ 6",
        "description": "สรุปขอบเขตประเภทเครือข่าย, กลไกการสลับวงจร 3 รูปแบบ, เทคนิคการหาเส้นทาง และระบบกระจายศูนย์",
        "content_html": """
        <div class="summary-card">
            <h3>📌 1. ประเภทของระบบเครือข่ายแบ่งตามขนาดและระยะทาง</h3>
            <div class="table-responsive">
                <table class="styled-table">
                    <thead>
                        <tr>
                            <th>ประเภทเครือข่าย</th>
                            <th>ชื่อเต็ม</th>
                            <th>ระยะทาง / ขอบเขต</th>
                            <th>ตัวอย่างการใช้งาน</th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr>
                            <td><span class="badge blue">PAN</span></td>
                            <td>Personal Area Network</td>
                            <td>ไม่เกิน 10 เมตร</td>
                            <td>Hotspot มือถือ, หูฟัง Bluetooth, อุปกรณ์สวมใส่</td>
                        </tr>
                        <tr>
                            <td><span class="badge green">LAN</span></td>
                            <td>Local Area Network</td>
                            <td>ไม่เกิน 10 กิโลเมตร</td>
                            <td>ห้องปฏิบัติการคอมพิวเตอร์, ภายในตึก, ภายในสำนักงาน</td>
                        </tr>
                        <tr>
                            <td><span class="badge amber">MAN</span></td>
                            <td>Metropolitan Area Network</td>
                            <td>ระดับเมือง / เทศบาล</td>
                            <td>ระบบเคเบิลทีวีเมือง, เครือข่ายเชื่อมโยงสาขาในเขตเทศบาล</td>
                        </tr>
                        <tr>
                            <td><span class="badge red">WAN</span></td>
                            <td>Wide Area Network</td>
                            <td>ข้ามจังหวัด ประเทศ ทั่วโลก</td>
                            <td>เครือข่ายอินเทอร์เน็ต, สายวงจรเช่า (Leased Line) เชื่อมสาขา</td>
                        </tr>
                    </tbody>
                </table>
            </div>

            <h3>📌 2. ระบบเครือข่ายแบบสวิตช์ (Switched Network) 3 รูปแบบ</h3>
            <div class="diagram-box">
                <div class="diagram-title">🎨 ภาพเปรียบเทียบการสลับสาย 3 รูปแบบ</div>
                <div class="svg-wrapper">
                    <svg viewBox="0 0 750 320" width="100%" height="auto" class="responsive-svg">
                        <!-- Circuit Switching -->
                        <g transform="translate(10, 20)">
                            <rect width="225" height="280" rx="12" fill="#f8fafc" stroke="#cbd5e1" stroke-width="2"/>
                            <rect width="225" height="40" rx="12" fill="#3b82f6"/>
                            <text x="112" y="25" fill="#ffffff" text-anchor="middle" font-size="14" font-weight="bold">Circuit-Switching</text>
                            <circle cx="40" cy="90" r="14" fill="#3b82f6"/><text x="40" y="95" fill="#fff" text-anchor="middle" font-size="10">A</text>
                            <circle cx="185" cy="90" r="14" fill="#3b82f6"/><text x="185" y="95" fill="#fff" text-anchor="middle" font-size="10">B</text>
                            <path d="M54 90 L171 90" stroke="#ef4444" stroke-width="4" stroke-dasharray="none"/>
                            <text x="112" y="130" fill="#0f172a" text-anchor="middle" font-size="12" font-weight="bold">จับจองสายตลอดเวลา</text>
                            <text x="112" y="150" fill="#475569" text-anchor="middle" font-size="11">ผู้อื่นใช้แทรกไม่ได้</text>
                            <text x="112" y="170" fill="#475569" text-anchor="middle" font-size="11">เช่น ระบบโทรศัพท์บ้าน</text>
                            <rect x="25" y="210" width="175" height="45" rx="6" fill="#e0f2fe"/>
                            <text x="112" y="235" fill="#0369a1" text-anchor="middle" font-size="11" font-weight="bold">Dedicated Circuit</text>
                        </g>
                        <!-- Message Switching -->
                        <g transform="translate(260, 20)">
                            <rect width="225" height="280" rx="12" fill="#f8fafc" stroke="#cbd5e1" stroke-width="2"/>
                            <rect width="225" height="40" rx="12" fill="#10b981"/>
                            <text x="112" y="25" fill="#ffffff" text-anchor="middle" font-size="14" font-weight="bold">Message-Switching</text>
                            <circle cx="40" cy="90" r="14" fill="#10b981"/><text x="40" y="95" fill="#fff" text-anchor="middle" font-size="10">A</text>
                            <rect x="90" y="75" width="45" height="30" rx="4" fill="#fbbf24"/>
                            <text x="112" y="94" fill="#000" text-anchor="middle" font-size="9">Store</text>
                            <circle cx="185" cy="90" r="14" fill="#10b981"/><text x="185" y="95" fill="#fff" text-anchor="middle" font-size="10">B</text>
                            <text x="112" y="130" fill="#0f172a" text-anchor="middle" font-size="12" font-weight="bold">Store and Forward</text>
                            <text x="112" y="150" fill="#475569" text-anchor="middle" font-size="11">ไม่ต้องจองวงจรล่วงหน้า</text>
                            <text x="112" y="170" fill="#475569" text-anchor="middle" font-size="11">เก็บไว้จนผู้รับพร้อมจึงส่ง</text>
                            <rect x="25" y="210" width="175" height="45" rx="6" fill="#d1fae5"/>
                            <text x="112" y="235" fill="#047857" text-anchor="middle" font-size="11" font-weight="bold">เก็บแล้วส่งต่อ</text>
                        </g>
                        <!-- Packet Switching -->
                        <g transform="translate(510, 20)">
                            <rect width="230" height="280" rx="12" fill="#f8fafc" stroke="#cbd5e1" stroke-width="2"/>
                            <rect width="230" height="40" rx="12" fill="#8b5cf6"/>
                            <text x="115" y="25" fill="#ffffff" text-anchor="middle" font-size="14" font-weight="bold">Packet-Switching</text>
                            <rect x="35" y="80" width="22" height="18" rx="2" fill="#f43f5e"/><text x="46" y="93" fill="#fff" text-anchor="middle" font-size="9">P1</text>
                            <rect x="62" y="80" width="22" height="18" rx="2" fill="#f59e0b"/><text x="73" y="93" fill="#fff" text-anchor="middle" font-size="9">P2</text>
                            <rect x="89" y="80" width="22" height="18" rx="2" fill="#3b82f6"/><text x="100" y="93" fill="#fff" text-anchor="middle" font-size="9">P3</text>
                            <text x="115" y="130" fill="#0f172a" text-anchor="middle" font-size="12" font-weight="bold">ซอยข้อมูลเป็นแพ็กเก็ต</text>
                            <text x="115" y="150" fill="#475569" text-anchor="middle" font-size="11">1. Datagram (ข้อมูลสั้นๆ)</text>
                            <text x="115" y="170" fill="#475569" text-anchor="middle" font-size="11">2. SVC (ชั่วคราว ข้อมูลมาก)</text>
                            <text x="115" y="190" fill="#475569" text-anchor="middle" font-size="11">3. PVC (ถาวร เหมือน Leased Line)</text>
                            <rect x="25" y="210" width="180" height="45" rx="6" fill="#ede9fe"/>
                            <text x="115" y="235" fill="#6d28d9" text-anchor="middle" font-size="11" font-weight="bold">Pipelining Technique</text>
                        </g>
                    </svg>
                </div>
            </div>

            <h3>📌 3. การค้นหาเส้นทาง (Routing) และจุดอ่อนที่ข้อสอบออก</h3>
            <ul class="styled-list">
                <li><strong>Centralized Routing (ศูนย์กลาง):</strong> โหนดศูนย์กลางเป็นคนเลือกเส้นทาง $\rightarrow$ <em>ข้อด้อย:</em> ถ้าศูนย์กลางล่ม ระบบหาเส้นทางจะล่มทั้งหมด</li>
                <li><strong>Static Routing (สถิตย์):</strong> กำหนดเส้นทางเดิมตายตัวเสมอ $\rightarrow$ <em>ข้อด้อย:</em> หากเส้นทางชำรุด จะส่งข้อมูลไม่ได้</li>
                <li><strong>Dynamic / Adaptive Routing (พลวัต):</strong> ค้นหาเส้นทางที่ดีที่สุดตามสถานการณ์ $\rightarrow$ <em>ข้อด้อย:</em> เสียเวลาคำนวณเส้นทางใหม่ก่อนส่งทุกครั้ง</li>
                <li><strong>Broadcast / Flooding (กระจายข่าว/ฟลัดดิง):</strong> ส่งออกไปทุกโหนด $\rightarrow$ <em>ข้อด้อย:</em> เกิดข้อมูลซ้ำซ้อนและเปลืองแบนด์วิดท์</li>
            </ul>
        </div>
        """
    },
    "ch7": {
        "title": "บทที่ 7: ระบบเครือข่าย LAN & Topology (Local Networks & Topologies)",
        "badge": "บทที่ 7",
        "description": "ข้อดี-ข้อจำกัดของโครงสร้างเครือข่าย BUS, RING, STAR, MESH, ประเภทเซิร์ฟเวอร์ และมาตรฐาน Ethernet",
        "content_html": """
        <div class="summary-card">
            <h3>📌 1. เปรียบเทียบ Topology ในการเชื่อมต่อเครือข่าย (ตาม Assignment 7)</h3>
            <p>ข้อสอบมักให้ดูรูป หรือถามข้อดีและข้อจำกัดของแต่ละรูปแบบโดยตรง:</p>

            <div class="diagram-box">
                <div class="diagram-title">🎨 แผนผังภาพ Topology หลักทั้ง 4 รูปแบบ</div>
                <div class="svg-wrapper">
                    <svg viewBox="0 0 750 420" width="100%" height="auto" class="responsive-svg">
                        <!-- BUS Topology -->
                        <g transform="translate(10, 20)">
                            <rect width="350" height="180" rx="10" fill="#f8fafc" stroke="#cbd5e1" stroke-width="2"/>
                            <text x="20" y="30" fill="#0f172a" font-weight="bold" font-size="14">BUS Topology</text>
                            <line x1="40" y1="100" x2="310" y2="100" stroke="#0284c7" stroke-width="6"/>
                            <!-- Terminators -->
                            <rect x="25" y="85" width="15" height="30" fill="#dc2626" rx="2"/>
                            <rect x="310" y="85" width="15" height="30" fill="#dc2626" rx="2"/>
                            <text x="32" y="130" fill="#dc2626" font-size="9" text-anchor="middle">Terminator</text>
                            <text x="318" y="130" fill="#dc2626" font-size="9" text-anchor="middle">Terminator</text>
                            <!-- Nodes -->
                            <circle cx="80" cy="60" r="12" fill="#3b82f6"/><line x1="80" y1="72" x2="80" y2="100" stroke="#0284c7" stroke-width="2"/>
                            <circle cx="175" cy="60" r="12" fill="#3b82f6"/><line x1="175" y1="72" x2="175" y2="100" stroke="#0284c7" stroke-width="2"/>
                            <circle cx="270" cy="60" r="12" fill="#3b82f6"/><line x1="270" y1="72" x2="270" y2="100" stroke="#0284c7" stroke-width="2"/>
                            <circle cx="130" cy="140" r="12" fill="#3b82f6"/><line x1="130" y1="128" x2="130" y2="100" stroke="#0284c7" stroke-width="2"/>
                            <circle cx="220" cy="140" r="12" fill="#3b82f6"/><line x1="220" y1="128" x2="220" y2="100" stroke="#0284c7" stroke-width="2"/>
                            <text x="175" y="172" fill="#0369a1" font-size="11" text-anchor="middle" font-weight="bold">สายเดี่ยว + มี Terminator ดูดกลืนสัญญาณสะท้อน</text>
                        </g>

                        <!-- STAR Topology -->
                        <g transform="translate(385, 20)">
                            <rect width="350" height="180" rx="10" fill="#f8fafc" stroke="#cbd5e1" stroke-width="2"/>
                            <text x="20" y="30" fill="#0f172a" font-weight="bold" font-size="14">STAR Topology</text>
                            <!-- Central Switch -->
                            <rect x="150" y="80" width="50" height="35" rx="6" fill="#10b981"/>
                            <text x="175" y="102" fill="#ffffff" font-size="10" text-anchor="middle" font-weight="bold">Switch</text>
                            <!-- Surrounding nodes -->
                            <circle cx="80" cy="50" r="12" fill="#3b82f6"/><line x1="80" y1="50" x2="150" y2="90" stroke="#64748b" stroke-width="2"/>
                            <circle cx="270" cy="50" r="12" fill="#3b82f6"/><line x1="270" y1="50" x2="200" y2="90" stroke="#64748b" stroke-width="2"/>
                            <circle cx="70" cy="120" r="12" fill="#3b82f6"/><line x1="70" y1="120" x2="150" y2="100" stroke="#64748b" stroke-width="2"/>
                            <circle cx="280" cy="120" r="12" fill="#3b82f6"/><line x1="280" y1="120" x2="200" y2="100" stroke="#64748b" stroke-width="2"/>
                            <circle cx="175" cy="150" r="12" fill="#3b82f6"/><line x1="175" y1="150" x2="175" y2="115" stroke="#64748b" stroke-width="2"/>
                            <text x="175" y="172" fill="#047857" font-size="11" text-anchor="middle" font-weight="bold">ศูนย์กลางคือ Switch/Hub | หากศูนย์กลางพัง ล่มทั้งระบบ</text>
                        </g>

                        <!-- RING Topology -->
                        <g transform="translate(10, 220)">
                            <rect width="350" height="180" rx="10" fill="#f8fafc" stroke="#cbd5e1" stroke-width="2"/>
                            <text x="20" y="30" fill="#0f172a" font-weight="bold" font-size="14">RING Topology</text>
                            <circle cx="175" cy="100" r="50" fill="none" stroke="#f59e0b" stroke-width="4"/>
                            <circle cx="175" cy="50" r="12" fill="#3b82f6"/>
                            <circle cx="225" cy="100" r="12" fill="#3b82f6"/>
                            <circle cx="175" cy="150" r="12" fill="#3b82f6"/>
                            <circle cx="125" cy="100" r="12" fill="#3b82f6"/>
                            <text x="175" y="103" fill="#d97706" font-size="11" text-anchor="middle" font-weight="bold">หมุนทางเดียว</text>
                            <text x="175" y="172" fill="#b45309" font-size="11" text-anchor="middle" font-weight="bold">FDDI ใช้ Fiber 2 วงหมุนสวนทางกัน ทำ Backbone</text>
                        </g>

                        <!-- MESH Topology -->
                        <g transform="translate(385, 220)">
                            <rect width="350" height="180" rx="10" fill="#f8fafc" stroke="#cbd5e1" stroke-width="2"/>
                            <text x="20" y="30" fill="#0f172a" font-weight="bold" font-size="14">MESH Topology</text>
                            <!-- 5 nodes interconnected -->
                            <!-- Points: (175,50), (235,80), (210,140), (140,140), (115,80) -->
                            <line x1="175" y1="50" x2="235" y2="80" stroke="#8b5cf6" stroke-width="1.5"/>
                            <line x1="175" y1="50" x2="210" y2="140" stroke="#8b5cf6" stroke-width="1.5"/>
                            <line x1="175" y1="50" x2="140" y2="140" stroke="#8b5cf6" stroke-width="1.5"/>
                            <line x1="175" y1="50" x2="115" y2="80" stroke="#8b5cf6" stroke-width="1.5"/>
                            <line x1="235" y1="80" x2="210" y2="140" stroke="#8b5cf6" stroke-width="1.5"/>
                            <line x1="235" y1="80" x2="140" y2="140" stroke="#8b5cf6" stroke-width="1.5"/>
                            <line x1="235" y1="80" x2="115" y2="80" stroke="#8b5cf6" stroke-width="1.5"/>
                            <line x1="210" y1="140" x2="140" y2="140" stroke="#8b5cf6" stroke-width="1.5"/>
                            <line x1="210" y1="140" x2="115" y2="80" stroke="#8b5cf6" stroke-width="1.5"/>
                            <line x1="140" y1="140" x2="115" y2="80" stroke="#8b5cf6" stroke-width="1.5"/>
                            <circle cx="175" cy="50" r="10" fill="#3b82f6"/>
                            <circle cx="235" cy="80" r="10" fill="#3b82f6"/>
                            <circle cx="210" cy="140" r="10" fill="#3b82f6"/>
                            <circle cx="140" cy="140" r="10" fill="#3b82f6"/>
                            <circle cx="115" cy="80" r="10" fill="#3b82f6"/>
                            <text x="175" y="172" fill="#6d28d9" font-size="11" text-anchor="middle" font-weight="bold">Point-to-Point ทุกคู่ | ปลอดภัยสูง | ใช้สายและแพงที่สุด</text>
                        </g>
                    </svg>
                </div>
            </div>

            <div class="table-responsive">
                <table class="styled-table">
                    <thead>
                        <tr>
                            <th>Topology</th>
                            <th>ข้อดี (Pros)</th>
                            <th>ข้อจำกัด (Cons)</th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr>
                            <td><strong>BUS</strong></td>
                            <td>• ราคาถูก ใช้สายสัญญาณน้อย<br>• ติดตั้งง่าย เพิ่มอุปกรณ์ใหม่ได้สะดวก<br>• คอมพ์ 1 เครื่องหยุดทำงาน เครือข่ายยังใช้ได้ต่อ</td>
                            <td>• <strong>ถ้าสายหลักขาด/ชำรุด พังทั้งระบบ</strong><br>• ตรวจหาจุดเสียยาก<br>• ข้อมูลชนกันง่ายถ้าส่งพร้อมกัน</td>
                        </tr>
                        <tr>
                            <td><strong>STAR</strong></td>
                            <td>• ติดตั้งและดูแลง่าย ซ่อมแซมสะดวก<br>• <strong>สายขาดเส้นหนึ่ง โหนดอื่นยังทำงานได้ปกติ</strong><br>• ตรวจหาจุดเสียหายได้ง่าย</td>
                            <td>• ราคาสูง ใช้สายมากกว่า Bus/Ring<br>• <strong>ถ้าศูนย์กลาง (Hub/Switch) ชำรุด ล่มทั้งระบบ</strong></td>
                        </tr>
                        <tr>
                            <td><strong>RING</strong></td>
                            <td>• ใช้สายสัญญาณน้อย ติดตั้งง่าย<br>• สื่อสารทางเดียว ข้อมูลไม่ชนกัน</td>
                            <td>• <strong>โหนดใดเสีย ระบบจะเสียหายทั้งหมด</strong><br>• เพิ่มเครื่องยาก ต้องปิดระบบก่อน<br>• เสียเวลาคัดลอก/ตรวจสอบทุกโหนด</td>
                        </tr>
                        <tr>
                            <td><strong>STAR-wire RING</strong></td>
                            <td>• รวมข้อดี Star+Ring เข้ากล่อง <strong>MAU</strong><br>• สวิตช์ภายใน MAU ตัดโหนดเสียแบบ Bypass วงแหวนไม่ขาด</td>
                            <td>• อุปกรณ์ MAU และการวางระบบมีความซับซ้อน</td>
                        </tr>
                        <tr>
                            <td><strong>MESH</strong></td>
                            <td>• สื่อสาร Point-to-Point โดยตรง ปลอดภัยสูงมาก<br>• สายเส้นใดขาด ระบบส่วนอื่นยังทำงานได้</td>
                            <td>• <strong>ใช้สายสัญญาณมากที่สุด และสิ้นเปลืองค่าใช้จ่ายมากที่สุด</strong></td>
                        </tr>
                    </tbody>
                </table>
            </div>

            <h3>📌 2. บริการเซิร์ฟเวอร์ (Server-Based) ที่สำคัญ</h3>
            <ul class="styled-list">
                <li><strong>Proxy Server:</strong> เก็บแคชหน้าเว็บที่เคยเปิด (Web Caching) ช่วยลดปริมาณ Data-stream และประหยัดแบนด์วิดท์</li>
                <li><strong>Disk Server:</strong> ควบคุมพื้นที่และจัดสรรโควตาฮาร์ดดิสก์ให้ผู้ใช้</li>
                <li><strong>File Server:</strong> จัดเก็บและแชร์แฟ้มข้อมูล</li>
                <li><strong>DNS Server:</strong> แปลงชื่อเว็บไซต์ (Domain) เป็น IP Address</li>
            </ul>
        </div>
        """
    },
    "ch8": {
        "title": "บทที่ 8: Subnetting & IP Addressing (WAN, IPv4/IPv6 & Calculations)",
        "badge": "บทที่ 8",
        "description": "สรุปหลักสูตรการคำนวณ Subnetting, แปลงเลขฐาน, วิเคราะห์ Classful & Classless และการอ่านสัญลักษณ์ Packet Tracer",
        "content_html": """
        <div class="summary-card">
            <h3>📌 1. เปรียบเทียบ IPv4 vs IPv6 และการย่อ</h3>
            <div class="table-responsive">
                <table class="styled-table">
                    <thead>
                        <tr>
                            <th>คุณสมบัติ</th>
                            <th>IPv4</th>
                            <th>IPv6</th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr>
                            <td><strong>ขนาด (Bits)</strong></td>
                            <td><strong>32 บิต</strong> (4 Octets x 8 บิต)</td>
                            <td><strong>128 บิต</strong> (8 Hextets x 16 บิต)</td>
                        </tr>
                        <tr>
                            <td><strong>จำนวนที่อยู่ทั้งหมด</strong></td>
                            <td>$2^{32} \\approx 4.29$ พันล้าน</td>
                            <td>$2^{128}$ หมายเลข (มหาศาล)</td>
                        </tr>
                        <tr>
                            <td><strong>รูปแบบตัวเลข</strong></td>
                            <td>ฐานสิบ Dotted-Decimal เช่น <code>192.168.1.1</code></td>
                            <td>ฐาน 16 Hexadecimal คั่นด้วย <code>:</code> เช่น <code>3FFE:85B::A9:1234</code></td>
                        </tr>
                        <tr>
                            <td><strong>กฎการย่อ IPv6</strong></td>
                            <td>-</td>
                            <td>• ตัดเลข 0 นำหน้าได้ เช่น <code>:00A9:</code> $\\rightarrow$ <code>:A9:</code><br>• ย่อกลุ่ม 0000 ติดกันเป็น <code>::</code> ได้ <strong>เพียง 1 ครั้งเท่านั้น!</strong></td>
                        </tr>
                    </tbody>
                </table>
            </div>

            <h3>📌 2. โครงสร้าง Classful Addressing (Class A, B, C)</h3>
            <div class="table-responsive">
                <table class="styled-table">
                    <thead>
                        <tr>
                            <th>Class</th>
                            <th>ช่วง Octet แรก</th>
                            <th>NetID (บิต)</th>
                            <th>HostID (บิต)</th>
                            <th>Default Subnet Mask</th>
                            <th>จำนวน Host ที่ใช้งานได้จริง</th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr>
                            <td><span class="badge blue">Class A</span></td>
                            <td><strong>0 – 127</strong> (ใช้จริง 1-126)</td>
                            <td>8 บิต (7 บิต)</td>
                            <td>24 บิต</td>
                            <td><code>255.0.0.0</code> (/8)</td>
                            <td>$2^{24} - 2 = 16,777,214$ โฮสต์</td>
                        </tr>
                        <tr>
                            <td><span class="badge green">Class B</span></td>
                            <td><strong>128 – 191</strong></td>
                            <td>16 บิต (14 บิต)</td>
                            <td>16 บิต</td>
                            <td><code>255.255.0.0</code> (/16)</td>
                            <td>$2^{16} - 2 = 65,534$ โฮสต์</td>
                        </tr>
                        <tr>
                            <td><span class="badge amber">Class C</span></td>
                            <td><strong>192 – 223</strong></td>
                            <td>24 บิต (21 บิต)</td>
                            <td>8 บิต</td>
                            <td><code>255.255.255.0</code> (/24)</td>
                            <td>$2^8 - 2 = 254$ โฮสต์</td>
                        </tr>
                        <tr>
                            <td><span class="badge purple">Class D</span></td>
                            <td><strong>224 – 239</strong></td>
                            <td colspan="4">สงวนไว้สำหรับกลุ่ม <strong>Multicast</strong></td>
                        </tr>
                        <tr>
                            <td><span class="badge gray">Class E</span></td>
                            <td><strong>240 – 255</strong></td>
                            <td colspan="4">สงวนไว้สำหรับการทดลองและพัฒนาในอนาคต (<strong>Reserved</strong>)</td>
                        </tr>
                    </tbody>
                </table>
            </div>

            <h3>📌 3. ตารางค่าน้ำหนัก 8 บิต และค่า Subnet Mask สะสม (เขียนลงกระดาษทดทันที!)</h3>
            <div class="magic-weights-box">
                <div class="weight-row">
                    <div class="w-item"><span class="w-val">128</span><span class="w-bit">2^7</span></div>
                    <div class="w-item"><span class="w-val">64</span><span class="w-bit">2^6</span></div>
                    <div class="w-item"><span class="w-val">32</span><span class="w-bit">2^5</span></div>
                    <div class="w-item"><span class="w-val">16</span><span class="w-bit">2^4</span></div>
                    <div class="w-item"><span class="w-val">8</span><span class="w-bit">2^3</span></div>
                    <div class="w-item"><span class="w-val">4</span><span class="w-bit">2^2</span></div>
                    <div class="w-item"><span class="w-val">2</span><span class="w-bit">2^1</span></div>
                    <div class="w-item"><span class="w-val">1</span><span class="w-bit">2^0</span></div>
                </div>
                <div class="mask-accum-table">
                    <p><strong>ค่าสะสมของ Subnet Mask เมื่อมีเลข 1:</strong></p>
                    <p class="code-line">1 บิต = <strong>128</strong> | 2 บิต = <strong>192</strong> | 3 บิต = <strong>224</strong> | 4 บิต = <strong>240</strong> | 5 บิต = <strong>248</strong> | 6 บิต = <strong>252</strong> | 7 บิต = <strong>254</strong> | 8 บิต = <strong>255</strong></p>
                </div>
            </div>

            <h3>📌 4. กฎเหล็กและเทคนิค Block Size ในการหา Network & Broadcast IP</h3>
            <div class="steps-box">
                <div class="step-card">
                    <div class="step-num">1</div>
                    <div class="step-text">
                        <strong>หา Block Size:</strong> <code>Block Size = 256 - ค่า Mask ใน Octet นั้น</code>
                    </div>
                </div>
                <div class="step-card">
                    <div class="step-num">2</div>
                    <div class="step-text">
                        <strong>หา Network Address:</strong> เป็น <code>พหุคูณของ Block Size</code> ที่ใกล้ที่สุดแต่ <strong>ไม่เกิน</strong> ค่า IP ในโจทย์
                    </div>
                </div>
                <div class="step-card">
                    <div class="step-num">3</div>
                    <div class="step-text">
                        <strong>หา Broadcast Address:</strong> <code>(Network Address ถัดไป) - 1</code>
                    </div>
                </div>
                <div class="step-card">
                    <div class="step-num">4</div>
                    <div class="step-text">
                        <strong>หา Usable Host Range:</strong> ตั้งแต่ <code>Network IP + 1</code> ถึง <code>Broadcast IP - 1</code> (จำนวนโฮสต์ $= 2^H - 2$)
                    </div>
                </div>
            </div>

            <h3>📌 5. สัญลักษณ์ Cisco Packet Tracer</h3>
            <div class="packet-tracer-grid">
                <div class="pt-card">
                    <div class="pt-icon">
                        <svg viewBox="0 0 100 80" width="80" height="60">
                            <ellipse cx="50" cy="40" rx="36" ry="24" fill="#3b82f6"/>
                            <!-- 4 arrows -->
                            <path d="M50 20 L50 32 M46 24 L50 20 L54 24" stroke="#fff" stroke-width="2.5" fill="none"/>
                            <path d="M50 60 L50 48 M46 56 L50 60 L54 56" stroke="#fff" stroke-width="2.5" fill="none"/>
                            <path d="M20 40 L34 40 M26 36 L20 40 L26 44" stroke="#fff" stroke-width="2.5" fill="none"/>
                            <path d="M80 40 L66 40 M74 36 L80 40 L74 44" stroke="#fff" stroke-width="2.5" fill="none"/>
                        </svg>
                    </div>
                    <div class="pt-name">Router (เราเตอร์)</div>
                    <div class="pt-desc">ทรงกระบอกกลม ลูกศร 4 ทิศทาง (Layer 3)</div>
                </div>
                <div class="pt-card">
                    <div class="pt-icon">
                        <svg viewBox="0 0 100 80" width="80" height="60">
                            <rect x="15" y="22" width="70" height="36" rx="4" fill="#10b981"/>
                            <!-- 4 opposing arrows -->
                            <path d="M25 32 L48 32 M42 28 L48 32 L42 36" stroke="#fff" stroke-width="2" fill="none"/>
                            <path d="M48 48 L25 48 M31 44 L25 48 L31 52" stroke="#fff" stroke-width="2" fill="none"/>
                            <path d="M52 32 L75 32 M69 28 L75 32 L69 36" stroke="#fff" stroke-width="2" fill="none"/>
                            <path d="M75 48 L52 48 M58 44 L52 48 L58 52" stroke="#fff" stroke-width="2" fill="none"/>
                        </svg>
                    </div>
                    <div class="pt-name">Switch (สวิตช์)</div>
                    <div class="pt-desc">กล่องสี่เหลี่ยม ลูกศร 4 เส้นสวนทางกัน (Layer 2)</div>
                </div>
                <div class="pt-card">
                    <div class="pt-icon">
                        <svg viewBox="0 0 100 80" width="80" height="60">
                            <rect x="15" y="22" width="70" height="36" rx="4" fill="#f59e0b"/>
                            <!-- Hub arrows outward -->
                            <line x1="30" y1="40" x2="70" y2="40" stroke="#fff" stroke-width="2"/>
                            <circle cx="50" cy="40" r="4" fill="#fff"/>
                            <path d="M70 40 L64 36 M70 40 L64 44" stroke="#fff" stroke-width="2"/>
                            <path d="M30 40 L36 36 M30 40 L36 44" stroke="#fff" stroke-width="2"/>
                        </svg>
                    </div>
                    <div class="pt-name">Hub (ฮับ)</div>
                    <div class="pt-desc">กล่องสี่เหลี่ยม กระจายสัญญาณทุกทาง (Layer 1)</div>
                </div>
                <div class="pt-card">
                    <div class="pt-icon">
                        <svg viewBox="0 0 100 80" width="80" height="60">
                            <path d="M25 50 a16 16 0 0 1 2 -24 a22 22 0 0 1 42 -4 a18 18 0 0 1 18 16 a14 14 0 0 1 -4 20 z" fill="#0284c7"/>
                        </svg>
                    </div>
                    <div class="pt-name">Network Cloud (คลาวด์)</div>
                    <div class="pt-desc">รูปก้อนเมฆ แทนโครงข่ายภายนอก WAN / Internet</div>
                </div>
            </div>
        </div>
        """
    }
}

summary_path = os.path.join(data_dir, "summary.js")
with open(summary_path, "w", encoding="utf-8") as f:
    f.write("// Illustrated Summaries and Diagrams for COM2703 (Chapters 5-8)\n")
    f.write("window.SUMMARY_DATA = ")
    json.dump(summary_data, f, ensure_ascii=False, indent=2)
    f.write(";\n")

print("Generated data/summary.js successfully!")
