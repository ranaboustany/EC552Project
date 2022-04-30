classdef BE552_Final_Project_exported < matlab.apps.AppBase

    % Properties that correspond to app components
    properties (Access = public)
        UIFigure    matlab.ui.Figure
        Image       matlab.ui.control.Image
        RUNButton   matlab.ui.control.Button
        Label       matlab.ui.control.Label
        Image_2     matlab.ui.control.Image
        TextArea    matlab.ui.control.TextArea
        withtheaminoacidslistedverticallyLabel  matlab.ui.control.Label
        Image_3     matlab.ui.control.Image
        ProteinBacteriaMatchingProgramLabel  matlab.ui.control.Label
        INFOButton  matlab.ui.control.Button
    end

    % Callbacks that handle component events
    methods (Access = private)

        % Button pushed function: RUNButton
        function RUNButtonPushed(app, event)
            BE552_Final_Project_Start
        end
    end

    % Component initialization
    methods (Access = private)

        % Create UIFigure and components
        function createComponents(app)

            % Create UIFigure and hide until all components are created
            app.UIFigure = uifigure('Visible', 'off');
            app.UIFigure.Color = [0.9882 0.9804 0.949];
            app.UIFigure.Position = [100 100 640 480];
            app.UIFigure.Name = 'MATLAB App';

            % Create Image
            app.Image = uiimage(app.UIFigure);
            app.Image.Position = [382 100 275 282];
            app.Image.ImageSource = 'image_processing20200929-16128-1a781ao (1).png';

            % Create RUNButton
            app.RUNButton = uibutton(app.UIFigure, 'push');
            app.RUNButton.ButtonPushedFcn = createCallbackFcn(app, @RUNButtonPushed, true);
            app.RUNButton.BackgroundColor = [0.6353 0.0784 0.1843];
            app.RUNButton.FontName = 'Calibri';
            app.RUNButton.FontSize = 30;
            app.RUNButton.FontWeight = 'bold';
            app.RUNButton.FontColor = [1 1 1];
            app.RUNButton.Position = [173 67 113 57];
            app.RUNButton.Text = 'RUN';

            % Create Label
            app.Label = uilabel(app.UIFigure);
            app.Label.FontName = 'Calibri';
            app.Label.FontSize = 15;
            app.Label.Position = [100 251 259 46];
            app.Label.Text = '*Please ensure all input files are text files';

            % Create Image_2
            app.Image_2 = uiimage(app.UIFigure);
            app.Image_2.Position = [366 199 275 282];
            app.Image_2.ImageSource = 'image_processing20200929-16128-1a781ao (1).png';

            % Create TextArea
            app.TextArea = uitextarea(app.UIFigure);
            app.TextArea.HorizontalAlignment = 'center';
            app.TextArea.FontName = 'Calibri';
            app.TextArea.FontSize = 18;
            app.TextArea.FontAngle = 'italic';
            app.TextArea.BackgroundColor = [0.9804 0.949 0.8784];
            app.TextArea.Position = [69 315 322 80];
            app.TextArea.Value = {'This program is deigned to help you find the most appropiate bacterial vector to use for producing a specfic protein.'};

            % Create withtheaminoacidslistedverticallyLabel
            app.withtheaminoacidslistedverticallyLabel = uilabel(app.UIFigure);
            app.withtheaminoacidslistedverticallyLabel.FontName = 'Calibri';
            app.withtheaminoacidslistedverticallyLabel.FontSize = 15;
            app.withtheaminoacidslistedverticallyLabel.Position = [112 241 236 22];
            app.withtheaminoacidslistedverticallyLabel.Text = 'with the amino acids listed vertically*';

            % Create Image_3
            app.Image_3 = uiimage(app.UIFigure);
            app.Image_3.Position = [390 23 275 282];
            app.Image_3.ImageSource = 'image_processing20200929-16128-1a781ao (1).png';

            % Create ProteinBacteriaMatchingProgramLabel
            app.ProteinBacteriaMatchingProgramLabel = uilabel(app.UIFigure);
            app.ProteinBacteriaMatchingProgramLabel.FontName = 'Calibri';
            app.ProteinBacteriaMatchingProgramLabel.FontSize = 32;
            app.ProteinBacteriaMatchingProgramLabel.FontWeight = 'bold';
            app.ProteinBacteriaMatchingProgramLabel.FontColor = [0.6353 0.0784 0.1843];
            app.ProteinBacteriaMatchingProgramLabel.Position = [18 404 483 65];
            app.ProteinBacteriaMatchingProgramLabel.Text = 'Protein-Bacteria Matching Program';

            % Create INFOButton
            app.INFOButton = uibutton(app.UIFigure, 'push');
            app.INFOButton.BackgroundColor = [0.6353 0.0784 0.1843];
            app.INFOButton.FontName = 'Calibri';
            app.INFOButton.FontSize = 30;
            app.INFOButton.FontWeight = 'bold';
            app.INFOButton.FontColor = [1 1 1];
            app.INFOButton.Position = [173 144 113 56];
            app.INFOButton.Text = 'INFO';

            % Show the figure after all components are created
            app.UIFigure.Visible = 'on';
        end
    end

    % App creation and deletion
    methods (Access = public)

        % Construct app
        function app = BE552_Final_Project_exported

            % Create UIFigure and components
            createComponents(app)

            % Register the app with App Designer
            registerApp(app, app.UIFigure)

            if nargout == 0
                clear app
            end
        end

        % Code that executes before app deletion
        function delete(app)

            % Delete UIFigure when app is deleted
            delete(app.UIFigure)
        end
    end
end