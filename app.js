// ==========================================================================
// Quiz Application State
// ==========================================================================

let state = {
  activeTab: 'memorization', // 'memorization', 'mathLogic', 'openEnded'
  
  // Independent state per tab
  tabState: {
    memorization: {
      questions: [],
      currentIndex: 0
    },
    mathLogic: {
      questions: [],
      currentIndex: 0
    },
    openEnded: {
      questions: [],
      currentIndex: 0
    }
  },
  
  // Global answers map across all tabs. Key: question ID, Value: { selected, isCorrect, draftText, rubricsChecked }
  userAnswers: {},
  theme: 'dark'
};

// ==========================================================================
// DOM Elements Cache
// ==========================================================================

const sidebar = document.getElementById('sidebar');
const menuBtn = document.getElementById('menuBtn');
const closeSidebarBtn = document.getElementById('closeSidebarBtn');
const activeScopeTitle = document.getElementById('activeScopeTitle');
const themeToggleBtn = document.getElementById('themeToggleBtn');
const themeSunIcon = themeToggleBtn.querySelector('.sun-icon');
const themeMoonIcon = themeToggleBtn.querySelector('.moon-icon');

// Tabs
const tabButtons = document.querySelectorAll('.tab-btn');
const sideTabCards = document.querySelectorAll('.sidebar-tab-stat-card');

// Stats Bar
const statsTracker = document.getElementById('statsTracker');
const progressVal = document.getElementById('progressVal');
const correctVal = document.getElementById('correctVal');
const incorrectVal = document.getElementById('incorrectVal');
const accuracyVal = document.getElementById('accuracyVal');
const correctLabel = document.getElementById('correctLabel');
const incorrectLabel = document.getElementById('incorrectLabel');

// Quiz Container
const quizContainer = document.getElementById('quizContainer');
const quizProgressBar = document.getElementById('quizProgressBar');
const questionCard = document.getElementById('questionCard');
const questionTypeBadge = document.getElementById('questionTypeBadge');
const questionLectureBadge = document.getElementById('questionLectureBadge');
const questionNumberDisplay = document.getElementById('questionNumberDisplay');
const questionText = document.getElementById('questionText');

// Choices wrappers
const mcqOptions = document.getElementById('mcqOptions');
const tfOptions = document.getElementById('tfOptions');
let tfTrueBtn = document.getElementById('tfTrueBtn');
let tfFalseBtn = document.getElementById('tfFalseBtn');

// Open Ended wrappers
const openEndedWrapper = document.getElementById('openEndedWrapper');
const essayAnswerInput = document.getElementById('essayAnswerInput');
const revealOpenAnswerBtn = document.getElementById('revealOpenAnswerBtn');
const openEndedReviewBox = document.getElementById('openEndedReviewBox');
const modelAnswerContent = document.getElementById('modelAnswerContent');
const rubricChecklist = document.getElementById('rubricChecklist');
const gradeCompleteBtn = document.getElementById('gradeCompleteBtn');
const gradeReviewBtn = document.getElementById('gradeReviewBtn');

// Explanation wrapper
const explanationBox = document.getElementById('explanationBox');
const explanationTitle = document.getElementById('explanationTitle');
const explanationContent = document.getElementById('explanationContent');

// Actions
const prevBtn = document.getElementById('prevBtn');
const nextBtn = document.getElementById('nextBtn');
const resetTopicBtn = document.getElementById('resetTopicBtn');

// Results Dashboard
const resultsContainer = document.getElementById('resultsContainer');
const resultsSubtitle = document.getElementById('resultsSubtitle');
const scoreRingBar = document.getElementById('scoreRingBar');
const scorePercent = document.getElementById('scorePercent');
const scoreRatio = document.getElementById('scoreRatio');
const gradeBadge = document.getElementById('gradeBadge');
const resTotalQ = document.getElementById('resTotalQ');
const resCorrect = document.getElementById('resCorrect');
const resIncorrect = document.getElementById('resIncorrect');
const resCorrectLabel = document.getElementById('resCorrectLabel');
const resIncorrectLabel = document.getElementById('resIncorrectLabel');
const retryQuizBtn = document.getElementById('retryQuizBtn');
const nextTopicBtn = document.getElementById('nextTopicBtn');
const reviewList = document.getElementById('reviewList');

// ==========================================================================
// Safe Storage Implementation
// ==========================================================================

const safeStorage = {
  _data: {},
  getItem(key) {
    try {
      return localStorage.getItem(key);
    } catch (e) {
      console.warn("Storage access blocked, using in-memory:", e);
      return this._data[key] || null;
    }
  },
  setItem(key, value) {
    try {
      localStorage.setItem(key, value);
    } catch (e) {
      console.warn("Storage access blocked, using in-memory:", e);
      this._data[key] = String(value);
    }
  },
  removeItem(key) {
    try {
      localStorage.removeItem(key);
    } catch (e) {
      console.warn("Storage access blocked, using in-memory:", e);
      delete this._data[key];
    }
  }
};

// ==========================================================================
// Theme Manager
// ==========================================================================

function initTheme() {
  try {
    const savedTheme = safeStorage.getItem('safety-quiz-theme') || 'dark';
    setTheme(savedTheme);
  } catch (e) {
    setTheme('dark');
  }
}

function setTheme(theme) {
  state.theme = theme;
  document.documentElement.setAttribute('data-theme', theme);
  safeStorage.setItem('safety-quiz-theme', theme);
  
  if (theme === 'dark') {
    themeSunIcon.style.display = 'block';
    themeMoonIcon.style.display = 'none';
  } else {
    themeSunIcon.style.display = 'none';
    themeMoonIcon.style.display = 'block';
  }
}

themeToggleBtn.addEventListener('click', () => {
  setTheme(state.theme === 'dark' ? 'light' : 'dark');
});

// Mobile Sidebar trigger
menuBtn.addEventListener('click', () => sidebar.classList.add('open'));
closeSidebarBtn.addEventListener('click', () => sidebar.classList.remove('open'));

// ==========================================================================
// State Persistence Helpers
// ==========================================================================

function getGlobalStorageKey() {
  return `safety-quiz-global-answers`;
}

function getTabStorageKey(tabName) {
  return `safety-quiz-progress-${tabName}`;
}

function saveProgress() {
  try {
    // 1. Save global answers map
    safeStorage.setItem(getGlobalStorageKey(), JSON.stringify(state.userAnswers));
    
    // 2. Save active tab parameters
    const tabName = state.activeTab;
    const tState = state.tabState[tabName];
    const key = getTabStorageKey(tabName);
    
    const progress = {
      shuffledOrder: tState.questions.map(q => q.id),
      currentIndex: tState.currentIndex
    };
    
    safeStorage.setItem(key, JSON.stringify(progress));
  } catch (e) {
    console.error("Error saving progress:", e);
  }
}

function loadProgress() {
  try {
    // 1. Load global answers
    const globalRaw = safeStorage.getItem(getGlobalStorageKey());
    if (globalRaw) {
      const parsed = JSON.parse(globalRaw);
      if (parsed && typeof parsed === 'object') {
        state.userAnswers = parsed;
      }
    }
    
    // 2. Load tab progress
    const tabName = state.activeTab;
    const tState = state.tabState[tabName];
    const key = getTabStorageKey(tabName);
    const raw = safeStorage.getItem(key);
    
    let parsed = null;
    if (raw) {
      try {
        parsed = JSON.parse(raw);
      } catch (e) {}
    }
    
    const fullList = safetyQuizData[tabName];
    
    if (parsed && parsed.shuffledOrder && Array.isArray(parsed.shuffledOrder)) {
      const order = parsed.shuffledOrder;
      tState.questions = order.map(id => {
        return fullList.find(q => q.id === id);
      }).filter(Boolean);
      
      if (tState.questions.length !== fullList.length) {
        tState.questions = shuffleArray([...fullList]);
        tState.currentIndex = 0;
      } else {
        const index = parsed.currentIndex;
        tState.currentIndex = typeof index === 'number' ? index : 0;
      }
    } else {
      tState.questions = shuffleArray([...fullList]);
      tState.currentIndex = 0;
    }
  } catch (e) {
    console.error("Error loading progress:", e);
    // Safe fallback
    const tabName = state.activeTab;
    const fullList = safetyQuizData[tabName];
    state.tabState[tabName].questions = shuffleArray([...fullList]);
    state.tabState[tabName].currentIndex = 0;
  }
}

function clearActiveProgress() {
  try {
    const tabName = state.activeTab;
    const key = getTabStorageKey(tabName);
    safeStorage.removeItem(key);
    
    // Clear user answers matching these specific questions
    const tState = state.tabState[tabName];
    tState.questions.forEach(q => {
      delete state.userAnswers[q.id];
    });
    
    // Re-save global answers
    safeStorage.setItem(getGlobalStorageKey(), JSON.stringify(state.userAnswers));
  } catch (e) {
    console.error("Error clearing progress:", e);
  }
}

function shuffleArray(array) {
  for (let i = array.length - 1; i > 0; i--) {
    const j = Math.floor(Math.random() * (i + 1));
    [array[i], array[j]] = [array[j], array[i]];
  }
  return array;
}

// ==========================================================================
// UI Rendering & Event Handling
// ==========================================================================

function initApp() {
  initTheme();
  
  if (typeof safetyQuizData === 'undefined') {
    console.error("safetyQuizData is missing!");
    activeScopeTitle.textContent = "Error: Database failed to load.";
    return;
  }
  
  switchTab(state.activeTab);
  
  // Set up tab click listeners
  tabButtons.forEach(btn => {
    btn.addEventListener('click', (e) => {
      switchTab(e.target.dataset.tab);
    });
  });
  
  // Set up sidebar tab card click listeners
  sideTabCards.forEach(card => {
    card.addEventListener('click', (e) => {
      const targetCard = e.target.closest('.sidebar-tab-stat-card');
      if (targetCard) {
        switchTab(targetCard.dataset.tabLink);
      }
    });
  });
}

function switchTab(tabName) {
  state.activeTab = tabName;
  
  // Update header text / tab selections
  tabButtons.forEach(btn => {
    if (btn.dataset.tab === tabName) {
      btn.classList.add('active');
    } else {
      btn.classList.remove('active');
    }
  });
  
  // Update sidebar active classes
  sideTabCards.forEach(card => {
    if (card.dataset.tabLink === tabName) {
      card.classList.add('active');
    } else {
      card.classList.remove('active');
    }
  });
  
  // Custom stats label renaming for openEnded (it has no strict correct/incorrect options)
  if (tabName === 'openEnded') {
    correctLabel.textContent = "Completed";
    incorrectLabel.textContent = "Review Flagged";
  } else {
    correctLabel.textContent = "Correct";
    incorrectLabel.textContent = "Incorrect";
  }
  
  loadTabContent();
}

function loadTabContent() {
  loadProgress();
  
  // Update title
  let tabText = "";
  if (state.activeTab === 'memorization') tabText = "Memorization Test";
  else if (state.activeTab === 'mathLogic') tabText = "Analytical & Math Logic";
  else if (state.activeTab === 'openEnded') tabText = "Open Book Scenarios";
  
  activeScopeTitle.textContent = `${tabText} (All Merged Lectures)`;
  
  showQuizOrResults();
  updateSidebarStats();
  updateOverallProgress();
}

function showQuizOrResults() {
  const tState = state.tabState[state.activeTab];
  
  // If there are no questions in this scope
  if (tState.questions.length === 0) {
    resultsContainer.style.display = 'none';
    quizContainer.style.display = 'flex';
    statsTracker.style.display = 'grid';
    
    questionNumberDisplay.textContent = "No questions";
    questionLectureBadge.style.display = 'none';
    questionTypeBadge.textContent = "EMPTY";
    questionText.textContent = "No questions found matching this filter for the selected lecture module.";
    mcqOptions.innerHTML = '';
    tfOptions.style.display = 'none';
    openEndedWrapper.style.display = 'none';
    openEndedReviewBox.style.display = 'none';
    explanationBox.style.display = 'none';
    nextBtn.disabled = true;
    prevBtn.disabled = true;
    
    progressVal.textContent = "0 / 0";
    correctVal.textContent = "0";
    incorrectVal.textContent = "0";
    accuracyVal.textContent = "0%";
    return;
  }
  
  questionLectureBadge.style.display = 'inline-block';
  
  if (tState.currentIndex >= tState.questions.length) {
    showResults();
  } else {
    resultsContainer.style.display = 'none';
    quizContainer.style.display = 'flex';
    statsTracker.style.display = 'grid';
    renderQuestion();
  }
}

function renderQuestion() {
  const tabName = state.activeTab;
  const tState = state.tabState[tabName];
  const question = tState.questions[tState.currentIndex];
  
  // Progress Bar
  const percent = (tState.currentIndex / tState.questions.length) * 100;
  quizProgressBar.style.width = `${percent}%`;
  
  // Badge references
  questionTypeBadge.textContent = question.type === 'MCQ' ? 'Multiple Choice' : question.type === 'TF' ? 'True / False' : 'Essay Scenario';
  questionLectureBadge.textContent = `L${question.lectureId}`;
  questionNumberDisplay.textContent = `Question ${tState.currentIndex + 1} of ${tState.questions.length}`;
  
  // Render text and equations
  questionText.innerHTML = formatMarkdownAndEquations(question.question);
  
  // Reset outputs
  nextBtn.disabled = true;
  prevBtn.disabled = tState.currentIndex === 0;
  explanationBox.style.display = 'none';
  
  const savedAnswer = state.userAnswers[question.id];
  
  if (state.activeTab === 'openEnded') {
    mcqOptions.style.display = 'none';
    tfOptions.style.display = 'none';
    openEndedWrapper.style.display = 'flex';
    
    renderOpenEnded(question, savedAnswer);
  } else {
    openEndedWrapper.style.display = 'none';
    openEndedReviewBox.style.display = 'none';
    
    if (question.type === 'MCQ') {
      tfOptions.style.display = 'none';
      mcqOptions.style.display = 'flex';
      renderMCQOptions(question, savedAnswer);
    } else {
      mcqOptions.style.display = 'none';
      tfOptions.style.display = 'grid';
      renderTFOptions(question, savedAnswer);
    }
  }
  
  updateStatsUI();
}

// ==========================================================================
// MCQ & True/False Render & Evaluation
// ==========================================================================

function renderMCQOptions(question, savedAnswer) {
  mcqOptions.innerHTML = '';
  
  Object.keys(question.options).forEach(letter => {
    const value = question.options[letter];
    const btn = document.createElement('button');
    btn.className = 'option-btn';
    btn.innerHTML = `
      <span class="option-letter">${letter}</span>
      <span class="option-text">${formatMarkdownAndEquations(value)}</span>
    `;
    
    if (savedAnswer) {
      btn.disabled = true;
      if (letter === question.answer) {
        btn.classList.add('correct');
      } else if (letter === savedAnswer.selected) {
        btn.classList.add('incorrect');
      }
    } else {
      btn.addEventListener('click', () => handleChoiceSelection(btn, letter, question));
    }
    
    mcqOptions.appendChild(btn);
  });
  
  if (savedAnswer) {
    showExplanationBox(savedAnswer.isCorrect, question.explanation);
    nextBtn.disabled = false;
  }
}

function renderTFOptions(question, savedAnswer) {
  tfTrueBtn.className = 'tf-btn';
  tfFalseBtn.className = 'tf-btn';
  tfTrueBtn.disabled = false;
  tfFalseBtn.disabled = false;
  
  if (savedAnswer) {
    tfTrueBtn.disabled = true;
    tfFalseBtn.disabled = true;
    
    if (question.answer === 'T') {
      tfTrueBtn.classList.add('correct');
      if (savedAnswer.selected === 'F') tfFalseBtn.classList.add('incorrect');
    } else {
      tfFalseBtn.classList.add('correct');
      if (savedAnswer.selected === 'T') tfTrueBtn.classList.add('incorrect');
    }
    showExplanationBox(savedAnswer.isCorrect, question.explanation);
    nextBtn.disabled = false;
  } else {
    tfTrueBtn.onclick = () => handleChoiceSelection(tfTrueBtn, 'T', question);
    tfFalseBtn.onclick = () => handleChoiceSelection(tfFalseBtn, 'F', question);
  }
}

function handleChoiceSelection(selectedBtn, chosenValue, question) {
  // Disable all options
  if (question.type === 'MCQ') {
    document.querySelectorAll('.option-btn').forEach(btn => btn.disabled = true);
  } else {
    tfTrueBtn.disabled = true;
    tfFalseBtn.disabled = true;
  }
  
  const isCorrect = chosenValue === question.answer;
  if (isCorrect) {
    selectedBtn.classList.add('correct');
  } else {
    selectedBtn.classList.add('incorrect');
    // Highlight correct answer
    if (question.type === 'MCQ') {
      document.querySelectorAll('.option-btn').forEach(btn => {
        if (btn.querySelector('.option-letter').textContent === question.answer) {
          btn.classList.add('correct');
        }
      });
    } else {
      if (question.answer === 'T') tfTrueBtn.classList.add('correct');
      else tfFalseBtn.classList.add('correct');
    }
  }
  
  state.userAnswers[question.id] = {
    selected: chosenValue,
    isCorrect: isCorrect
  };
  
  showExplanationBox(isCorrect, question.explanation);
  nextBtn.disabled = false;
  
  saveProgress();
  updateStatsUI();
  updateSidebarPercentages();
}

function showExplanationBox(isCorrect, text) {
  explanationBox.style.display = 'flex';
  explanationBox.className = `explanation-box ${isCorrect ? 'correct-box' : 'incorrect-box'}`;
  explanationTitle.textContent = isCorrect ? 'Correct Answer Explanation' : 'Incorrect Answer Explanation';
  explanationContent.innerHTML = formatMarkdownAndEquations(text);
}

// ==========================================================================
// Open Ended Scenario Handling (Rubrics & self grading)
// ==========================================================================

function renderOpenEnded(question, savedAnswer) {
  essayAnswerInput.value = savedAnswer ? (savedAnswer.draftText || '') : '';
  essayAnswerInput.disabled = !!savedAnswer;
  
  if (savedAnswer) {
    openEndedReviewBox.style.display = 'flex';
    revealOpenAnswerBtn.style.display = 'none';
    
    // Display model answer
    modelAnswerContent.innerHTML = formatMarkdownAndEquations(question.modelAnswer);
    
    // Populate rubrics
    rubricChecklist.innerHTML = '';
    question.gradingRubric.forEach((rubric, rIdx) => {
      const label = document.createElement('label');
      label.className = 'rubric-item';
      
      const isChecked = savedAnswer.rubricsChecked && savedAnswer.rubricsChecked.includes(rIdx);
      label.innerHTML = `
        <input type="checkbox" data-rubric-index="${rIdx}" ${isChecked ? 'checked' : ''} ${savedAnswer.locked ? 'disabled' : ''}>
        <span>${rubric}</span>
      `;
      
      const checkbox = label.querySelector('input');
      checkbox.addEventListener('change', () => {
        if (!state.userAnswers[question.id].rubricsChecked) {
          state.userAnswers[question.id].rubricsChecked = [];
        }
        if (checkbox.checked) {
          state.userAnswers[question.id].rubricsChecked.push(rIdx);
        } else {
          state.userAnswers[question.id].rubricsChecked = state.userAnswers[question.id].rubricsChecked.filter(idx => idx !== rIdx);
        }
        saveProgress();
      });
      
      rubricChecklist.appendChild(label);
    });
    
    // Enable self grade click logic
    if (savedAnswer.locked) {
      // Highlight selection state on self grading buttons
      gradeCompleteBtn.disabled = true;
      gradeReviewBtn.disabled = true;
      if (savedAnswer.isCorrect) {
        gradeCompleteBtn.className = 'btn btn-primary'; // Greenish emerald selection style
        gradeReviewBtn.className = 'btn btn-secondary';
      } else {
        gradeCompleteBtn.className = 'btn btn-secondary';
        gradeReviewBtn.className = 'btn btn-error-light';
      }
      nextBtn.disabled = false;
    } else {
      gradeCompleteBtn.disabled = false;
      gradeReviewBtn.disabled = false;
      gradeCompleteBtn.className = 'btn btn-success-light';
      gradeReviewBtn.className = 'btn btn-error-light';
      
      gradeCompleteBtn.onclick = () => finalizeOpenEndedSelfGrade(true, question.id);
      gradeReviewBtn.onclick = () => finalizeOpenEndedSelfGrade(false, question.id);
    }
  } else {
    openEndedReviewBox.style.display = 'none';
    revealOpenAnswerBtn.style.display = 'block';
    
    // Bind reveal button click
    revealOpenAnswerBtn.onclick = () => {
      const val = essayAnswerInput.value.trim();
      if (!val) {
        alert("Please draft your answer in the text box before revealing the model answer.");
        return;
      }
      
      state.userAnswers[question.id] = {
        draftText: val,
        selected: 'Reviewed',
        isCorrect: false, // Default until they click grade buttons
        rubricsChecked: [],
        locked: false
      };
      
      saveProgress();
      renderQuestion(); // Re-render to show checklists
    };
  }
}

function finalizeOpenEndedSelfGrade(isCompleted, questionId) {
  if (state.userAnswers[questionId]) {
    state.userAnswers[questionId].isCorrect = isCompleted;
    state.userAnswers[questionId].locked = true;
    
    saveProgress();
    renderQuestion();
    updateStatsUI();
    updateSidebarPercentages();
    updateOverallProgress();
  }
}

// ==========================================================================
// Stats Dashboard Rendering
// ==========================================================================

function getTabStats() {
  const tabName = state.activeTab;
  const tState = state.tabState[tabName];
  
  let correct = 0;
  let incorrect = 0;
  let answered = 0;
  
  tState.questions.forEach(q => {
    const ans = state.userAnswers[q.id];
    if (ans) {
      answered++;
      // For open-ended questions, they have "locked" flag which locks self grading
      if (tabName === 'openEnded') {
        if (ans.locked) {
          if (ans.isCorrect) correct++;
          else incorrect++;
        }
      } else {
        if (ans.isCorrect) correct++;
        else incorrect++;
      }
    }
  });
  
  const accuracy = answered > 0 ? Math.round((correct / answered) * 100) : 0;
  return { correct, incorrect, answered, total: tState.questions.length, accuracy };
}

function updateStatsUI() {
  const stats = getTabStats();
  
  progressVal.textContent = `${stats.answered} / ${stats.total}`;
  correctVal.textContent = stats.correct;
  incorrectVal.textContent = stats.incorrect;
  accuracyVal.textContent = `${stats.accuracy}%`;
}

function calculateTabStatsSummary(tabName) {
  const fullList = safetyQuizData[tabName];
  let correct = 0;
  let incorrect = 0;
  let answered = 0;
  
  fullList.forEach(q => {
    const ans = state.userAnswers[q.id];
    if (ans) {
      answered++;
      if (tabName === 'openEnded') {
        if (ans.locked) {
          if (ans.isCorrect) correct++;
          else incorrect++;
        }
      } else {
        if (ans.isCorrect) correct++;
        else incorrect++;
      }
    }
  });
  
  const completionPercent = fullList.length > 0 ? Math.round((answered / fullList.length) * 100) : 0;
  const accuracyPercent = answered > 0 ? Math.round((correct / answered) * 100) : 0;
  
  return {
    answered,
    total: fullList.length,
    completionPercent,
    accuracyPercent
  };
}

function updateSidebarStats() {
  // Update Memorization stats
  const memStats = calculateTabStatsSummary('memorization');
  const sideMemPct = document.getElementById('sideMemPct');
  const sideMemBar = document.getElementById('sideMemBar');
  const sideMemRatio = document.getElementById('sideMemRatio');
  const sideMemAccuracy = document.getElementById('sideMemAccuracy');
  
  if (sideMemPct) sideMemPct.textContent = `${memStats.completionPercent}%`;
  if (sideMemBar) sideMemBar.style.width = `${memStats.completionPercent}%`;
  if (sideMemRatio) sideMemRatio.textContent = `${memStats.answered} / ${memStats.total} Completed`;
  if (sideMemAccuracy) sideMemAccuracy.textContent = `Acc: ${memStats.accuracyPercent}%`;

  // Update Math & Logic stats
  const mathStats = calculateTabStatsSummary('mathLogic');
  const sideMathPct = document.getElementById('sideMathPct');
  const sideMathBar = document.getElementById('sideMathBar');
  const sideMathRatio = document.getElementById('sideMathRatio');
  const sideMathAccuracy = document.getElementById('sideMathAccuracy');
  
  if (sideMathPct) sideMathPct.textContent = `${mathStats.completionPercent}%`;
  if (sideMathBar) sideMathBar.style.width = `${mathStats.completionPercent}%`;
  if (sideMathRatio) sideMathRatio.textContent = `${mathStats.answered} / ${mathStats.total} Completed`;
  if (sideMathAccuracy) sideMathAccuracy.textContent = `Acc: ${mathStats.accuracyPercent}%`;

  // Update Open Book stats
  const openStats = calculateTabStatsSummary('openEnded');
  const sideOpenPct = document.getElementById('sideOpenPct');
  const sideOpenBar = document.getElementById('sideOpenBar');
  const sideOpenRatio = document.getElementById('sideOpenRatio');
  const sideOpenAccuracy = document.getElementById('sideOpenAccuracy');
  
  if (sideOpenPct) sideOpenPct.textContent = `${openStats.completionPercent}%`;
  if (sideOpenBar) sideOpenBar.style.width = `${openStats.completionPercent}%`;
  if (sideOpenRatio) sideOpenRatio.textContent = `${openStats.answered} / ${openStats.total} Completed`;
  if (sideOpenAccuracy) sideOpenAccuracy.textContent = `Strong: ${openStats.accuracyPercent}%`;
}

function updateOverallProgress() {
  const tabs = ['memorization', 'mathLogic', 'openEnded'];
  let totalQuestions = 0;
  let totalAnswered = 0;
  
  tabs.forEach(tabName => {
    const list = safetyQuizData[tabName];
    totalQuestions += list.length;
    
    list.forEach(q => {
      const ans = state.userAnswers[q.id];
      if (ans) {
        if (tabName === 'openEnded') {
          if (ans.locked) totalAnswered++;
        } else {
          totalAnswered++;
        }
      }
    });
  });
  
  const percent = totalQuestions > 0 ? Math.round((totalAnswered / totalQuestions) * 100) : 0;
  
  const overallProgressBar = document.getElementById('overallProgressBar');
  const overallProgressText = document.getElementById('overallProgressText');
  
  if (overallProgressBar) overallProgressBar.style.width = `${percent}%`;
  if (overallProgressText) overallProgressText.textContent = `${percent}% Complete`;
}

// Navigation event bindings
prevBtn.addEventListener('click', () => {
  const tState = state.tabState[state.activeTab];
  if (tState.currentIndex > 0) {
    tState.currentIndex--;
    saveProgress();
    showQuizOrResults();
  }
});

nextBtn.addEventListener('click', () => {
  const tState = state.tabState[state.activeTab];
  tState.currentIndex++;
  saveProgress();
  showQuizOrResults();
});

// Reset Tab
resetTopicBtn.addEventListener('click', () => {
  if (confirm(`Are you sure you want to reset your progress for the active tab? This will reshuffle questions.`)) {
    clearActiveProgress();
    
    const tabName = state.activeTab;
    const fullList = safetyQuizData[tabName];
    
    state.tabState[tabName].questions = shuffleArray([...fullList]);
    state.tabState[tabName].currentIndex = 0;
    
    saveProgress();
    loadTabContent();
  }
});

// ==========================================================================
// Results Scorecard Rendering
// ==========================================================================

function showResults() {
  quizContainer.style.display = 'none';
  statsTracker.style.display = 'none';
  resultsContainer.style.display = 'flex';
  
  const stats = getTabStats();
  
  // Visual accuracy ring (Circumference = 2 * PI * r = 2 * 3.14159 * 70 = 439.8)
  const offset = 439.8 - (stats.accuracy / 100) * 439.8;
  scoreRingBar.style.strokeDashoffset = offset;
  
  scorePercent.textContent = `${stats.accuracy}%`;
  
  if (state.activeTab === 'openEnded') {
    scoreRatio.textContent = `${stats.correct} / ${stats.total} Completed`;
    resCorrectLabel.textContent = "Completed / Strong";
    resIncorrectLabel.textContent = "Needs Review / Flagged";
  } else {
    scoreRatio.textContent = `${stats.correct} / ${stats.total} Correct`;
    resCorrectLabel.textContent = "Correct Answers";
    resIncorrectLabel.textContent = "Incorrect Answers";
  }
  
  // Custom feedback subtitle
  if (stats.accuracy >= 90) {
    resultsSubtitle.textContent = "Outstanding performance! You've achieved deep mastery over this safety module.";
  } else if (stats.accuracy >= 75) {
    resultsSubtitle.textContent = "Well done! You have a solid grasp of these safety concepts, but a few areas need review.";
  } else {
    resultsSubtitle.textContent = "Keep studying! Review your incorrect answers in the list below and try again.";
  }
  
  // Letter grade calculation
  let grade = 'F';
  if (stats.accuracy >= 97) grade = 'A+';
  else if (stats.accuracy >= 93) grade = 'A';
  else if (stats.accuracy >= 90) grade = 'A-';
  else if (stats.accuracy >= 87) grade = 'B+';
  else if (stats.accuracy >= 83) grade = 'B';
  else if (stats.accuracy >= 80) grade = 'B-';
  else if (stats.accuracy >= 77) grade = 'C+';
  else if (stats.accuracy >= 73) grade = 'C';
  else if (stats.accuracy >= 70) grade = 'C-';
  else if (stats.accuracy >= 60) grade = 'D';
  gradeBadge.textContent = grade;
  
  resTotalQ.textContent = stats.total;
  resCorrect.textContent = stats.correct;
  resIncorrect.textContent = stats.incorrect;
  
  renderReviewList();
}

function renderReviewList() {
  reviewList.innerHTML = '';
  const tabName = state.activeTab;
  const tState = state.tabState[tabName];
  
  tState.questions.forEach((q, idx) => {
    const ans = state.userAnswers[q.id];
    const isCorrect = ans ? ans.isCorrect : false;
    const selected = ans ? ans.selected : 'Unanswered';
    
    const item = document.createElement('div');
    item.className = `review-item ${isCorrect ? 'correct-item' : 'incorrect-item'}`;
    
    let answerRowContent = '';
    
    if (tabName === 'openEnded') {
      const checkedRubricsCount = ans && ans.rubricsChecked ? ans.rubricsChecked.length : 0;
      answerRowContent = `
        <div class="review-ans-row">
          <span class="review-ans-label">Your Draft:</span>
          <span class="review-ans-val">${ans ? formatMarkdownAndEquations(ans.draftText) : 'No answer'}</span>
        </div>
        <div class="review-ans-row">
          <span class="review-ans-label">Grading Status:</span>
          <span class="review-ans-val ${isCorrect ? 'text-success' : 'text-error'}">${isCorrect ? 'Completed &amp; Strong' : 'Flagged for Review'} (${checkedRubricsCount} of ${q.gradingRubric.length} rubrics met)</span>
        </div>
        <div class="review-ans-row explanation-row">
          <span class="review-ans-label">Model Key:</span>
          <span class="review-ans-val text-sub">${formatMarkdownAndEquations(q.modelAnswer)}</span>
        </div>
      `;
    } else if (q.type === 'MCQ') {
      const selectedText = q.options[selected] || selected;
      const correctText = q.options[q.answer] || q.answer;
      answerRowContent = `
        <div class="review-ans-row">
          <span class="review-ans-label">Your Answer:</span>
          <span class="review-ans-val ${isCorrect ? 'text-success' : 'text-error'}">(${selected}) ${formatMarkdownAndEquations(selectedText)}</span>
        </div>
        <div class="review-ans-row">
          <span class="review-ans-label">Correct Answer:</span>
          <span class="review-ans-val text-success">(${q.answer}) ${formatMarkdownAndEquations(correctText)}</span>
        </div>
        <div class="review-ans-row explanation-row">
          <span class="review-ans-label">Explanation:</span>
          <span class="review-ans-val text-sub">${formatMarkdownAndEquations(q.explanation)}</span>
        </div>
      `;
    } else {
      const selectedText = selected === 'T' ? 'True' : selected === 'F' ? 'False' : selected;
      const correctText = q.answer === 'T' ? 'True' : 'False';
      answerRowContent = `
        <div class="review-ans-row">
          <span class="review-ans-label">Your Answer:</span>
          <span class="review-ans-val ${isCorrect ? 'text-success' : 'text-error'}">${selectedText}</span>
        </div>
        <div class="review-ans-row">
          <span class="review-ans-label">Correct Answer:</span>
          <span class="review-ans-val text-success">${correctText}</span>
        </div>
        <div class="review-ans-row explanation-row">
          <span class="review-ans-label">Explanation:</span>
          <span class="review-ans-val text-sub">${formatMarkdownAndEquations(q.explanation)}</span>
        </div>
      `;
    }
    
    item.innerHTML = `
      <div class="review-q-header">
        <span class="review-q-num">Question ${idx + 1} (L${q.lectureId})</span>
        <span class="review-q-status">${isCorrect ? 'Completed' : 'Review Flagged'}</span>
      </div>
      <div class="review-q-text">${formatMarkdownAndEquations(q.question)}</div>
      <div class="review-answers">
        ${answerRowContent}
      </div>
    `;
    
    reviewList.appendChild(item);
  });
}

// Scorecard Control Bindings
retryQuizBtn.addEventListener('click', () => {
  const tabName = state.activeTab;
  state.tabState[tabName].currentIndex = 0;
  clearActiveProgress();
  
  // Reload
  const fullList = safetyQuizData[tabName];
  state.tabState[tabName].questions = shuffleArray([...fullList]);
  saveProgress();
  loadTabContent();
});

nextTopicBtn.addEventListener('click', () => {
  // Cycles between: memorization -> mathLogic -> openEnded -> memorization
  let nextTab = 'memorization';
  if (state.activeTab === 'memorization') nextTab = 'mathLogic';
  else if (state.activeTab === 'mathLogic') nextTab = 'openEnded';
  
  switchTab(nextTab);
});

// ==========================================================================
// Text Formatting & Math Equations Parser
// ==========================================================================

function parseMath(equation) {
  let esc = escapeHtml(equation.trim());
  
  // Replace LaTeX control sequences with Unicode symbols
  esc = esc.replace(/\\times/g, ' × ')
           .replace(/\\cdot/g, ' · ')
           .replace(/\\div/g, ' ÷ ')
           .replace(/\\pm/g, ' ± ')
           .replace(/\\approx/g, ' ≈ ')
           .replace(/\\geq?/g, ' ≥ ')
           .replace(/\\leq?/g, ' ≤ ')
           .replace(/\\ge/g, ' ≥ ')
           .replace(/\\le/g, ' ≤ ')
           .replace(/\\Delta/g, 'Δ')
           .replace(/\\theta/g, 'θ')
           .replace(/\\pi/g, 'π')
           .replace(/\\alpha/g, 'α')
           .replace(/\\beta/g, 'β')
           .replace(/\\text\s*{(.*?)}/g, '<span class="math-text">$1</span>')
           .replace(/\\bar\s*{(.*?)}/g, '<span style="text-decoration: overline;">$1</span>');
  
  // Subscripts: N_{rc} -> N<sub>rc</sub>
  esc = esc.replace(/([a-zA-Z0-9_]+)_{([^{}]+)}/g, '$1<sub>$2</sub>');
  esc = esc.replace(/([a-zA-Z0-9]+)_([a-zA-Z0-9])/g, '$1<sub>$2</sub>');
  
  // Superscripts: g^2 -> g<sup>2</sup>, 10^5 -> 10<sup>5</sup>
  esc = esc.replace(/([a-zA-Z0-9_]+)\^{([^{}]+)}/g, '$1<sup>$2</sup>');
  esc = esc.replace(/([a-zA-Z0-9]+)\^([a-zA-Z0-9])/g, '$1<sup>$2</sup>');
  
  // Clean up any double spaces
  esc = esc.replace(/\s+/g, ' ');
  
  return esc;
}

function formatMarkdownAndEquations(text) {
  if (!text) return '';
  
  // Clean special characters
  let html = text;
  
  // Process LaTeX-like equations block: $$ ... $$
  html = html.replace(/\$\$([\s\S]*?)\$\$/g, (match, equation) => {
    return `<div class="formula-block">${parseMath(equation)}</div>`;
  });
  
  // Process inline equations: $ ... $
  html = html.replace(/\$([\s\S]*?)\$/g, (match, equation) => {
    return `<span class="math-inline">${parseMath(equation)}</span>`;
  });
  
  // Bold formatting: **text**
  html = html.replace(/\*\*(.*?)\*\*/g, '<strong>$1</strong>');
  
  // Italic formatting: _text_
  html = html.replace(/_(.*?)_/g, '<em>$1</em>');
  
  // List elements formatting inside model answers
  html = html.replace(/### (.*?)\n/g, '<h3>$1</h3>');
  
  return html;
}

function escapeHtml(text) {
  return text
    .replace(/&/g, "&amp;")
    .replace(/</g, "&lt;")
    .replace(/>/g, "&gt;")
    .replace(/"/g, "&quot;")
    .replace(/'/g, "&#039;");
}

// Start application
window.addEventListener('DOMContentLoaded', initApp);
