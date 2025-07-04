# UI/UX Testing Report – LinkedIn Post Generator

## ✅ Environment

- Framework: Streamlit
- Browser: Chrome
- Resolution: 1920x1080

## 🧪 UI Elements Tested

| Feature             | Description                                 | Result | Notes                           |
| ------------------- | ------------------------------------------- | ------ | ------------------------------- |
| Dropdown (Topic)    | List of tags loads properly                 | ✅     | Pulls from FewShotPosts         |
| Dropdown (Length)   | Shows Short, Medium, Long                   | ✅     | Functional                      |
| Dropdown (Language) | English / Hinglish toggle                   | ✅     | Functional                      |
| Generate Button     | Triggers output post                        | ✅     | Smooth                          |
| Output Display      | Proper formatting of generated post         | ✅     | Hinglish is displayed correctly |
| Error Handling      | Handles empty/missing selections gracefully | ✅     | Default post shown              |
| Responsiveness      | UI adjusts for various screen sizes         | ✅     | Basic Streamlit responsiveness  |
| Styling             | Layout is clean and simple                  | ✅     | Could improve fonts/padding     |

## 🔍 Observations

- The layout is minimalistic but could be enhanced with:
  - Custom fonts or branding
  - Improved spacing between elements
  - Section separators or icons for better UX

## 💡 Suggestions

- Add a “Clear” or “Reset” button
- Use `st.markdown` for styled text output
- Add tooltips for dropdowns
- Make output area scrollable if the post is too long

## ScreenShots

![UI Screenshot](images/ui_ux.png)
![UI Screenshot](images/ui_ux2.png)
