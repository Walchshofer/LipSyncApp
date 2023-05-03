class LipSyncGUI:
  
    def __init__(self, num_faces=2):
        self.num_faces = num_faces
        self.selected_face_index = 0

        self.init_face_buttons()
        self.init_audio_dropdowns()

    def init_face_buttons(self):
        self.face_buttons = []
        for i in range(self.num_faces):
            image_path = f'face_{i+1}.png'
            face_button = CustomImageButton(
                image_path,
                layout=Layout(width='100px', height='100px'),
                description=f'Face {i+1}'
            )
            face_button.on_click(self.on_face_button_click)
            self.face_buttons.append(face_button)

    def init_audio_dropdowns(self):
        self.audio_dropdowns = []
        for i in range(self.num_faces):
            audio_dropdown = Dropdown(
                options=['process audio'] if i == self.selected_face_index else ['silent audio', 'do not process'],
                layout=Layout(width='auto'),
            )
            audio_dropdown.observe(self.on_audio_dropdown_change, names='value')
            self.audio_dropdowns.append(audio_dropdown)

    def on_face_button_click(self, button):
        old_selected_face_index = self.selected_face_index
        self.selected_face_index = self.face_buttons.index(button)

        self.audio_dropdowns[old_selected_face_index].options = ['silent audio', 'do not process']
        self.audio_dropdowns[self.selected_face_index].options = ['process audio']

    def on_audio_dropdown_change(self, change):
        dropdown = change.owner
        dropdown_index = self.audio_dropdowns.index(dropdown)
        selected_audio = change['new']

        if dropdown_index == self.selected_face_index:
            # Do something with the selected audio for the selected face
            pass
        else:
            # Do something with the selected audio for the non-selected face
            pass

# Create an instance of the LipSyncGUI class and display the GUI
lip_sync_gui = LipSyncGUI(number_of_faces)
lip_sync_gui.display()
