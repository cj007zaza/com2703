/* ==========================================================================
   COM2703 Computer Network - Final Review Application
   Main JavaScript Controller (Tabs, Flashcards, Quiz & Subnet Calculator)
   ========================================================================== */

document.addEventListener('DOMContentLoaded', () => {
    // ----------------------------------------------------------------------
    // 1. Theme Toggle
    // ----------------------------------------------------------------------
    const themeToggleBtn = document.getElementById('themeToggleBtn');
    const themeIcon = themeToggleBtn.querySelector('.theme-icon');
    const savedTheme = localStorage.getItem('com2703_theme') || 'theme-dark';
    document.body.className = savedTheme;
    updateThemeIcon(savedTheme);

    themeToggleBtn.addEventListener('click', () => {
        const isDark = document.body.classList.contains('theme-dark');
        const newTheme = isDark ? 'theme-light' : 'theme-dark';
        document.body.className = newTheme;
        localStorage.setItem('com2703_theme', newTheme);
        updateThemeIcon(newTheme);
    });

    function updateThemeIcon(theme) {
        themeIcon.textContent = theme === 'theme-dark' ? '🌙' : '☀️';
    }

    // ----------------------------------------------------------------------
    // 2. Tab Navigation
    // ----------------------------------------------------------------------
    const navTabs = document.querySelectorAll('.nav-tab');
    const tabPanes = document.querySelectorAll('.tab-pane');

    navTabs.forEach(tab => {
        tab.addEventListener('click', () => {
            const targetId = tab.dataset.tab;
            navTabs.forEach(t => t.classList.remove('active'));
            tabPanes.forEach(p => p.classList.remove('active'));

            tab.classList.add('active');
            const targetPane = document.getElementById(targetId);
            if (targetPane) {
                targetPane.classList.add('active');
            }
        });
    });

    // ----------------------------------------------------------------------
    // 3. TAB 1: Summary Chapter Navigation
    // ----------------------------------------------------------------------
    const chapterChips = document.querySelectorAll('.chapter-chip');
    const summaryDynamicContent = document.getElementById('summaryDynamicContent');

    function renderSummaryChapter(chKey) {
        if (!window.SUMMARY_DATA || !window.SUMMARY_DATA[chKey]) return;
        summaryDynamicContent.innerHTML = window.SUMMARY_DATA[chKey].content_html;
    }

    chapterChips.forEach(chip => {
        chip.addEventListener('click', () => {
            chapterChips.forEach(c => c.classList.remove('active'));
            chip.classList.add('active');
            renderSummaryChapter(chip.dataset.chapter);
        });
    });

    // Default Chapter 5
    renderSummaryChapter('ch5');

    // ----------------------------------------------------------------------
    // 4. TAB 2: Flashcards Logic
    // ----------------------------------------------------------------------
    const allFlashcards = window.FLASHCARDS_DATA || [];
    let currentFcList = [...allFlashcards];
    let fcIndex = 0;
    const masteredFcSet = new Set(JSON.parse(localStorage.getItem('com2703_fc_mastered') || '[]'));

    const flashcardEl = document.getElementById('flashcardElement');
    const fcChapterFilter = document.getElementById('fcChapterFilter');
    const fcCurrentIndexEl = document.getElementById('fcCurrentIndex');
    const fcTotalCountEl = document.getElementById('fcTotalCount');
    const fcMasteredCountEl = document.getElementById('fcMasteredCount');
    const fcFrontBadge = document.getElementById('fcFrontBadge');
    const fcFrontTerm = document.getElementById('fcFrontTerm');
    const fcBackDef = document.getElementById('fcBackDef');
    const fcBackMnemonic = document.getElementById('fcBackMnemonic');
    const fcPrevBtn = document.getElementById('fcPrevBtn');
    const fcNextBtn = document.getElementById('fcNextBtn');
    const fcShuffleBtn = document.getElementById('fcShuffleBtn');
    const fcMarkBtn = document.getElementById('fcMarkBtn');

    function updateFlashcardUI() {
        if (currentFcList.length === 0) {
            fcFrontTerm.textContent = "ไม่มีการ์ดในหมวดนี้";
            fcBackDef.textContent = "กรุณาเลือกหมวดอื่น";
            fcBackMnemonic.textContent = "-";
            fcCurrentIndexEl.textContent = "0";
            fcTotalCountEl.textContent = "0";
            return;
        }

        const item = currentFcList[fcIndex];
        flashcardEl.classList.remove('flipped');

        fcFrontBadge.textContent = item.chapter;
        fcFrontTerm.textContent = item.term;
        fcBackDef.textContent = item.definition;
        fcBackMnemonic.textContent = item.mnemonic;

        fcCurrentIndexEl.textContent = fcIndex + 1;
        fcTotalCountEl.textContent = currentFcList.length;
        fcMasteredCountEl.textContent = masteredFcSet.size;

        if (masteredFcSet.has(item.id)) {
            fcMarkBtn.classList.remove('btn-success');
            fcMarkBtn.classList.add('btn-secondary');
            fcMarkBtn.textContent = '🌟 จำแล้ว (คลิกเพื่อยกเลิก)';
        } else {
            fcMarkBtn.classList.add('btn-success');
            fcMarkBtn.classList.remove('btn-secondary');
            fcMarkBtn.textContent = '✅ จำได้แล้ว';
        }

        fcPrevBtn.disabled = fcIndex === 0;
        fcNextBtn.disabled = fcIndex === currentFcList.length - 1;
    }

    flashcardEl.addEventListener('click', () => {
        flashcardEl.classList.toggle('flipped');
    });

    fcPrevBtn.addEventListener('click', () => {
        if (fcIndex > 0) {
            fcIndex--;
            updateFlashcardUI();
        }
    });

    fcNextBtn.addEventListener('click', () => {
        if (fcIndex < currentFcList.length - 1) {
            fcIndex++;
            updateFlashcardUI();
        }
    });

    fcShuffleBtn.addEventListener('click', () => {
        currentFcList.sort(() => Math.random() - 0.5);
        fcIndex = 0;
        updateFlashcardUI();
    });

    fcMarkBtn.addEventListener('click', () => {
        if (currentFcList.length === 0) return;
        const currentItem = currentFcList[fcIndex];
        if (masteredFcSet.has(currentItem.id)) {
            masteredFcSet.delete(currentItem.id);
        } else {
            masteredFcSet.add(currentItem.id);
        }
        localStorage.setItem('com2703_fc_mastered', JSON.stringify([...masteredFcSet]));
        updateFlashcardUI();
    });

    fcChapterFilter.addEventListener('change', () => {
        const val = fcChapterFilter.value;
        if (val === 'all') {
            currentFcList = [...allFlashcards];
        } else {
            currentFcList = allFlashcards.filter(c => c.chapter === val);
        }
        fcIndex = 0;
        updateFlashcardUI();
    });

    // Keyboard shortcuts for flashcards
    window.addEventListener('keydown', (e) => {
        const activeTab = document.querySelector('.nav-tab.active');
        if (!activeTab || activeTab.dataset.tab !== 'tab-flashcards') return;

        if (e.code === 'Space') {
            e.preventDefault();
            flashcardEl.classList.toggle('flipped');
        } else if (e.code === 'ArrowRight') {
            if (fcIndex < currentFcList.length - 1) {
                fcIndex++;
                updateFlashcardUI();
            }
        } else if (e.code === 'ArrowLeft') {
            if (fcIndex > 0) {
                fcIndex--;
                updateFlashcardUI();
            }
        }
    });

    updateFlashcardUI();

    // ----------------------------------------------------------------------
    // 5. TAB 3: Quiz Engine (90 Questions)
    // ----------------------------------------------------------------------
    const rawQuestions = window.QUESTIONS_90 || [];
    let activeQuestions = [...rawQuestions];
    let currentQIndex = 0;
    let quizMode = 'practice'; // 'practice' or 'exam'
    let userAnswers = {}; // { qId: selectedOptionIndex }
    let flaggedSet = new Set();
    let examTimerInterval = null;
    let timeRemainingSeconds = 90 * 60; // 90 minutes

    // Elements
    const modePracticeBtn = document.getElementById('modePracticeBtn');
    const modeExamBtn = document.getElementById('modeExamBtn');
    const quizChapterFilter = document.getElementById('quizChapterFilter');
    const openGridBtn = document.getElementById('openGridBtn');
    const answeredCounter = document.getElementById('answeredCounter');

    const quizCounterText = document.getElementById('quizCounterText');
    const quizChapBadge = document.getElementById('quizChapBadge');
    const quizTimerDisplay = document.getElementById('quizTimerDisplay');
    const quizProgressFill = document.getElementById('quizProgressFill');

    const qNumBadge = document.getElementById('qNumBadge');
    const questionText = document.getElementById('questionText');
    const optionsContainer = document.getElementById('optionsContainer');
    const explanationCard = document.getElementById('explanationCard');
    const expResultBadge = document.getElementById('expResultBadge');
    const explanationText = document.getElementById('explanationText');

    const quizPrevBtn = document.getElementById('quizPrevBtn');
    const quizNextBtn = document.getElementById('quizNextBtn');
    const quizFlagBtn = document.getElementById('quizFlagBtn');
    const quizSubmitBtn = document.getElementById('quizSubmitBtn');

    // Modals
    const gridDrawerModal = document.getElementById('gridDrawerModal');
    const closeDrawerBtn = document.getElementById('closeDrawerBtn');
    const drawerGridContainer = document.getElementById('drawerGridContainer');

    const examResultModal = document.getElementById('examResultModal');
    const resultScoreText = document.getElementById('resultScoreText');
    const resultPercentText = document.getElementById('resultPercentText');
    const resultFeedbackText = document.getElementById('resultFeedbackText');
    const resStatCorrect = document.getElementById('resStatCorrect');
    const resStatWrong = document.getElementById('resStatWrong');
    const resStatSkipped = document.getElementById('resStatSkipped');
    const chapBreakdownBox = document.getElementById('chapBreakdownBox');
    const resultReviewBtn = document.getElementById('resultReviewBtn');
    const resultRetakeBtn = document.getElementById('resultRetakeBtn');

    function filterQuestions() {
        const val = quizChapterFilter.value;
        if (val === 'all') {
            activeQuestions = [...rawQuestions];
        } else {
            activeQuestions = rawQuestions.filter(q => q.chapter.startsWith(val));
        }
        currentQIndex = 0;
        renderQuestion();
        updateDrawerGrid();
    }

    quizChapterFilter.addEventListener('change', filterQuestions);

    modePracticeBtn.addEventListener('click', () => {
        setQuizMode('practice');
    });

    modeExamBtn.addEventListener('click', () => {
        setQuizMode('exam');
    });

    function setQuizMode(mode) {
        quizMode = mode;
        if (mode === 'practice') {
            modePracticeBtn.classList.add('active');
            modeExamBtn.classList.remove('active');
            quizTimerDisplay.classList.add('hidden');
            quizSubmitBtn.classList.add('hidden');
            if (examTimerInterval) clearInterval(examTimerInterval);
        } else {
            modeExamBtn.classList.add('active');
            modePracticeBtn.classList.remove('active');
            quizTimerDisplay.classList.remove('hidden');
            quizSubmitBtn.classList.remove('hidden');
            startExamTimer();
        }
        renderQuestion();
    }

    function startExamTimer() {
        if (examTimerInterval) clearInterval(examTimerInterval);
        timeRemainingSeconds = 90 * 60;
        updateTimerDisplay();

        examTimerInterval = setInterval(() => {
            timeRemainingSeconds--;
            updateTimerDisplay();
            if (timeRemainingSeconds <= 0) {
                clearInterval(examTimerInterval);
                alert('⏰ หมดเวลาทำข้อสอบแล้ว! กำลังส่งกระดาษคำตอบ');
                submitExam();
            }
        }, 1000);
    }

    function updateTimerDisplay() {
        const mins = Math.floor(timeRemainingSeconds / 60);
        const secs = timeRemainingSeconds % 60;
        quizTimerDisplay.textContent = `⏱️ ${String(mins).padStart(2, '0')}:${String(secs).padStart(2, '0')}`;
    }

    function renderQuestion() {
        if (activeQuestions.length === 0) {
            questionText.textContent = "ไม่มีข้อสอบในบทที่เลือก";
            optionsContainer.innerHTML = "";
            explanationCard.classList.add('hidden');
            return;
        }

        const q = activeQuestions[currentQIndex];
        const selected = userAnswers[q.id];

        // Header info
        qNumBadge.textContent = `Q${currentQIndex + 1}`;
        quizCounterText.textContent = `ข้อที่ ${currentQIndex + 1} / ${activeQuestions.length}`;
        quizChapBadge.textContent = q.chapter.split(':')[0];
        questionText.textContent = q.question;

        // Progress bar
        const pct = Math.round(((currentQIndex + 1) / activeQuestions.length) * 100);
        quizProgressFill.style.width = `${pct}%`;

        // Flag button
        if (flaggedSet.has(q.id)) {
            quizFlagBtn.classList.add('btn-primary');
            quizFlagBtn.classList.remove('btn-outline');
            quizFlagBtn.textContent = '🚩 ปักหมุดแล้ว';
        } else {
            quizFlagBtn.classList.remove('btn-primary');
            quizFlagBtn.classList.add('btn-outline');
            quizFlagBtn.textContent = '🔖 ปักหมุดทบทวน';
        }

        // Render Options
        optionsContainer.innerHTML = '';
        const optionKeys = ['A', 'B', 'C', 'D'];

        q.options.forEach((optText, optIdx) => {
            const optBtn = document.createElement('div');
            optBtn.className = 'option-item';

            if (selected !== undefined) {
                if (selected === optIdx) {
                    optBtn.classList.add('selected');
                }

                if (quizMode === 'practice') {
                    if (optIdx === q.answer) {
                        optBtn.classList.add('correct');
                    } else if (selected === optIdx) {
                        optBtn.classList.add('wrong');
                    }
                }
            }

            optBtn.innerHTML = `
                <span class="option-key">${optionKeys[optIdx]}</span>
                <span class="option-content">${optText}</span>
            `;

            optBtn.addEventListener('click', () => {
                selectOption(q.id, optIdx);
            });

            optionsContainer.appendChild(optBtn);
        });

        // Explanation Card (in practice mode)
        if (quizMode === 'practice' && selected !== undefined) {
            explanationCard.classList.remove('hidden');
            const isCorrect = selected === q.answer;
            expResultBadge.textContent = isCorrect ? 'ถูกต้อง!' : 'ยังไม่ถูกต้อง';
            expResultBadge.className = `exp-badge ${isCorrect ? 'correct' : 'wrong'}`;
            explanationText.textContent = q.explanation;
        } else {
            explanationCard.classList.add('hidden');
        }

        // Navigation buttons
        quizPrevBtn.disabled = currentQIndex === 0;
        quizNextBtn.disabled = currentQIndex === activeQuestions.length - 1;

        // Counter
        answeredCounter.textContent = Object.keys(userAnswers).length;
    }

    function selectOption(qId, optIdx) {
        userAnswers[qId] = optIdx;
        renderQuestion();
        updateDrawerGrid();
    }

    quizPrevBtn.addEventListener('click', () => {
        if (currentQIndex > 0) {
            currentQIndex--;
            renderQuestion();
        }
    });

    quizNextBtn.addEventListener('click', () => {
        if (currentQIndex < activeQuestions.length - 1) {
            currentQIndex++;
            renderQuestion();
        }
    });

    quizFlagBtn.addEventListener('click', () => {
        const q = activeQuestions[currentQIndex];
        if (flaggedSet.has(q.id)) {
            flaggedSet.delete(q.id);
        } else {
            flaggedSet.add(q.id);
        }
        renderQuestion();
        updateDrawerGrid();
    });

    // Drawer Grid Modal
    openGridBtn.addEventListener('click', () => {
        updateDrawerGrid();
        gridDrawerModal.classList.remove('hidden');
    });

    closeDrawerBtn.addEventListener('click', () => {
        gridDrawerModal.classList.add('hidden');
    });

    gridDrawerModal.addEventListener('click', (e) => {
        if (e.target === gridDrawerModal) {
            gridDrawerModal.classList.add('hidden');
        }
    });

    function updateDrawerGrid() {
        drawerGridContainer.innerHTML = '';
        activeQuestions.forEach((q, idx) => {
            const btn = document.createElement('button');
            btn.className = 'grid-cell-btn';
            btn.textContent = idx + 1;

            if (userAnswers[q.id] !== undefined) {
                btn.classList.add('answered');
            }
            if (flaggedSet.has(q.id)) {
                btn.classList.add('flagged');
            }
            if (idx === currentQIndex) {
                btn.classList.add('current');
            }

            btn.addEventListener('click', () => {
                currentQIndex = idx;
                renderQuestion();
                gridDrawerModal.classList.add('hidden');
            });

            drawerGridContainer.appendChild(btn);
        });
    }

    // Submit Exam
    quizSubmitBtn.addEventListener('click', () => {
        const unanswered = activeQuestions.filter(q => userAnswers[q.id] === undefined).length;
        if (unanswered > 0) {
            const confirmSubmit = confirm(`คุณยังมีข้อที่ไม่ได้ทำอีก ${unanswered} ข้อ ต้องการส่งข้อสอบหรือไม่?`);
            if (!confirmSubmit) return;
        }
        submitExam();
    });

    function submitExam() {
        if (examTimerInterval) clearInterval(examTimerInterval);

        let correct = 0;
        let wrong = 0;
        let skipped = 0;

        const chapStats = {};

        activeQuestions.forEach(q => {
            const cName = q.chapter.split(':')[0].trim();
            if (!chapStats[cName]) {
                chapStats[cName] = { correct: 0, total: 0 };
            }
            chapStats[cName].total++;

            const ans = userAnswers[q.id];
            if (ans === undefined) {
                skipped++;
            } else if (ans === q.answer) {
                correct++;
                chapStats[cName].correct++;
            } else {
                wrong++;
            }
        });

        const total = activeQuestions.length;
        const pct = Math.round((correct / total) * 100);

        resultScoreText.textContent = `${correct} / ${total}`;
        resultPercentText.textContent = `${pct}%`;
        resStatCorrect.textContent = correct;
        resStatWrong.textContent = wrong;
        resStatSkipped.textContent = skipped;

        let msg = "";
        if (pct >= 80) msg = "🌟 ยอดเยี่ยมมาก! คุณพร้อมสอบ Final และมีโอกาสได้ A สูงมาก!";
        else if (pct >= 65) msg = "👍 ทำได้ดี! ทบทวนข้อที่ผิดและฝึกคำนวณบทที่ 8 เพิ่มเติมอีกนิด";
        else msg = "📖 ควรทบทวนสรุปและลองฝึกทำข้อสอบอีกรอบ โดยเฉพาะข้อคำนวณ Subnetting";
        resultFeedbackText.textContent = msg;

        // Render chapter breakdown
        chapBreakdownBox.innerHTML = '<strong>📊 สรุปคะแนนแยกตามบท:</strong>';
        for (const [cName, stat] of Object.entries(chapStats)) {
            const item = document.createElement('div');
            item.className = 'chap-breakdown-item';
            const cPct = Math.round((stat.correct / stat.total) * 100);
            item.innerHTML = `
                <span>${cName}</span>
                <strong>${stat.correct}/${stat.total} (${cPct}%)</strong>
            `;
            chapBreakdownBox.appendChild(item);
        }

        examResultModal.classList.remove('hidden');
    }

    resultReviewBtn.addEventListener('click', () => {
        examResultModal.classList.add('hidden');
        setQuizMode('practice');
        currentQIndex = 0;
        renderQuestion();
    });

    resultRetakeBtn.addEventListener('click', () => {
        examResultModal.classList.add('hidden');
        userAnswers = {};
        flaggedSet.clear();
        currentQIndex = 0;
        setQuizMode('exam');
    });

    renderQuestion();

    // ----------------------------------------------------------------------
    // 6. TAB 4: IPv4 Subnet Calculator Tool
    // ----------------------------------------------------------------------
    const calcIpInput = document.getElementById('calcIpInput');
    const calcPrefixSelect = document.getElementById('calcPrefixSelect');
    const calcComputeBtn = document.getElementById('calcComputeBtn');
    const calcResultBox = document.getElementById('calcResultBox');

    // Populate Prefix options /8 to /30
    for (let p = 8; p <= 30; p++) {
        const opt = document.createElement('option');
        opt.value = p;
        opt.textContent = `/${p} (${getMaskFromPrefix(p)})`;
        if (p === 28) opt.selected = true; // Default /28
        calcPrefixSelect.appendChild(opt);
    }

    function getMaskFromPrefix(prefix) {
        let mask = [];
        for (let i = 0; i < 4; i++) {
            const n = Math.min(prefix, 8);
            mask.push(256 - Math.pow(2, 8 - n));
            prefix -= n;
        }
        return mask.join('.');
    }

    function computeSubnet() {
        const ipStr = calcIpInput.value.trim();
        const prefix = parseInt(calcPrefixSelect.value, 10);

        const ipParts = ipStr.split('.').map(Number);
        if (ipParts.length !== 4 || ipParts.some(p => isNaN(p) || p < 0 || p > 255)) {
            alert('กรุณากรอกหมายเลข IPv4 ให้ถูกต้อง เช่น 192.168.100.25');
            return;
        }

        const ipNum = ((ipParts[0] << 24) >>> 0) + ((ipParts[1] << 16) >>> 0) + ((ipParts[2] << 8) >>> 0) + (ipParts[3] >>> 0);
        const maskNum = prefix === 0 ? 0 : ((0xFFFFFFFF << (32 - prefix)) >>> 0);

        const netNum = (ipNum & maskNum) >>> 0;
        const wildcardNum = (~maskNum) >>> 0;
        const bcastNum = (netNum | wildcardNum) >>> 0;

        const hostBits = 32 - prefix;
        const totalHosts = Math.pow(2, hostBits);
        const usableHosts = hostBits <= 1 ? 0 : totalHosts - 2;

        const firstHostNum = usableHosts > 0 ? netNum + 1 : netNum;
        const lastHostNum = usableHosts > 0 ? bcastNum - 1 : bcastNum;

        function numToIp(n) {
            return [
                (n >>> 24) & 255,
                (n >>> 16) & 255,
                (n >>> 8) & 255,
                n & 255
            ].join('.');
        }

        // Octet block size method explanation
        const octetIndex = Math.floor((prefix - 1) / 8);
        const maskParts = getMaskFromPrefix(prefix).split('.').map(Number);
        const octetMask = maskParts[octetIndex];
        const blockSize = 256 - octetMask;

        calcResultBox.innerHTML = `
            <div class="res-row">
                <span class="res-lbl">IP Address ที่ระบุ:</span>
                <span class="res-val highlight">${ipStr} /${prefix}</span>
            </div>
            <div class="res-row">
                <span class="res-lbl">Subnet Mask:</span>
                <span class="res-val">${getMaskFromPrefix(prefix)}</span>
            </div>
            <div class="res-row">
                <span class="res-lbl">Network Address (ตัวแรก):</span>
                <span class="res-val success">${numToIp(netNum)}</span>
            </div>
            <div class="res-row">
                <span class="res-lbl">Broadcast Address (ตัวสุดท้าย):</span>
                <span class="res-val">${numToIp(bcastNum)}</span>
            </div>
            <div class="res-row">
                <span class="res-lbl">ช่วง Host ที่ใช้งานได้จริง:</span>
                <span class="res-val">${numToIp(firstHostNum)} &mdash; ${numToIp(lastHostNum)}</span>
            </div>
            <div class="res-row">
                <span class="res-lbl">จำนวน Host ทั้งหมด ($2^H$):</span>
                <span class="res-val">${totalHosts.toLocaleString()} ตัว (บิต $H = ${hostBits}$)</span>
            </div>
            <div class="res-row">
                <span class="res-lbl">จำนวน Host ที่ใช้ได้จริง ($2^H - 2$):</span>
                <span class="res-val success">${usableHosts.toLocaleString()} ตัว</span>
            </div>
            <div class="res-row">
                <span class="res-lbl">ระยะก้าว (Block Size):</span>
                <span class="res-val">${blockSize} (ใน Octet ที่ ${octetIndex + 1})</span>
            </div>
            <div style="margin-top: 8px; font-size: 0.85rem; color: var(--text-secondary); line-height: 1.5;">
                💡 <strong>วิธีคิด:</strong> Prefix /${prefix} ตกใน Octet ที่ ${octetIndex + 1} มีค่า Mask = ${octetMask} ดังนั้น Block size = 256 - ${octetMask} = <strong>${blockSize}</strong> โดย Network Address ใน Octet นี้คือพหุคูณของ ${blockSize} ที่ไม่เกิน ${ipParts[octetIndex]} นั่นคือ <strong>${(netNum >>> ((3 - octetIndex) * 8)) & 255}</strong>
            </div>
        `;
    }

    calcComputeBtn.addEventListener('click', computeSubnet);
    computeSubnet(); // initial run
});
