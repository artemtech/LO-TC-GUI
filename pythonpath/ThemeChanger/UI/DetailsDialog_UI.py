# -*- coding: utf-8 -*-
# !/usr/bin/env python

# =============================================================================
#
# Dialog implementation generated from a XDL file.
#
# Created: Fri Nov 15 12:59:58 2019
#      by: unodit 0.8.0
#
# WARNING! All changes made in this file will be overwritten
#          if the file is generated again!
#
# =============================================================================

import uno
import unohelper
from com.sun.star.awt import XActionListener
from com.sun.star.task import XJobExecutor


class DetailsDialog_UI(unohelper.Base, XActionListener, XJobExecutor):
    """
    Class documentation...AAAAAAAAAAAAAAAAAAAAAAA
    """

    def __init__(self, ctx=uno.getComponentContext(), theme_data={}):
        self.theme_name = theme_data["name"] if (not theme_data.get("name") == None) else "Dummy theme"
        self.theme_description = theme_data["description"] if (not theme_data.get("description") == None) else "Hello world,\n this is dummy theme"
        self.theme_author = theme_data["author"] if (not theme_data.get("author") == None) else "libreoffice.id"

        self.LocalContext = ctx
        self.ServiceManager = self.LocalContext.ServiceManager
        self.Toolkit = self.ServiceManager.createInstanceWithContext("com.sun.star.awt.ExtToolkit", self.LocalContext)

        # -----------------------------------------------------------
        #               Create dialog and insert controls
        # -----------------------------------------------------------

        # --------------create dialog container and set model and properties
        self.DialogContainer = self.ServiceManager.createInstanceWithContext("com.sun.star.awt.UnoControlDialog",
                                                                             self.LocalContext)
        self.DialogModel = self.ServiceManager.createInstance("com.sun.star.awt.UnoControlDialogModel")
        self.DialogContainer.setModel(self.DialogModel)

        self.DialogModel.Name = "ThemeChangerDetails"
        self.DialogModel.PositionX = "10"
        self.DialogModel.PositionY = "10"
        self.DialogModel.Width = 250
        self.DialogModel.Height = 180
        self.DialogModel.Closeable = True
        self.DialogModel.Moveable = True
        self.DialogModel.Title = "%s - Details" % self.theme_name

        # --------- create an instance of Button control, set properties ---
        self.InstallButton = self.DialogModel.createInstance("com.sun.star.awt.UnoControlButtonModel")

        self.InstallButton.Name = "InstallButton"
        self.InstallButton.TabIndex = 0
        self.InstallButton.PositionX = "155"
        self.InstallButton.PositionY = "159"
        self.InstallButton.Width = 38
        self.InstallButton.Height = 15
        self.InstallButton.Label = "Install"

        # inserts the control model into the dialog model
        self.DialogModel.insertByName("InstallButton", self.InstallButton)

        # add the action listener
        self.DialogContainer.getControl('InstallButton').addActionListener(self)
        self.DialogContainer.getControl('InstallButton').setActionCommand('InstallButton_OnClick')

        # --------- create an instance of Button control, set properties ---
        self.RemoveButton = self.DialogModel.createInstance("com.sun.star.awt.UnoControlButtonModel")

        self.RemoveButton.Name = "RemoveButton"
        self.RemoveButton.TabIndex = 1
        self.RemoveButton.PositionX = "9"
        self.RemoveButton.PositionY = "159"
        self.RemoveButton.Width = 38
        self.RemoveButton.Height = 15
        self.RemoveButton.Label = "Remove"

        # inserts the control model into the dialog model
        self.DialogModel.insertByName("RemoveButton", self.RemoveButton)

        # add the action listener
        self.DialogContainer.getControl('RemoveButton').addActionListener(self)
        self.DialogContainer.getControl('RemoveButton').setActionCommand('RemoveButton_OnClick')

        # --------- create an instance of Button control, set properties ---
        self.CloseButton = self.DialogModel.createInstance("com.sun.star.awt.UnoControlButtonModel")

        self.CloseButton.Name = "CloseButton"
        self.CloseButton.TabIndex = 2
        self.CloseButton.PositionX = "200"
        self.CloseButton.PositionY = "159"
        self.CloseButton.Width = 38
        self.CloseButton.Height = 15
        self.CloseButton.Label = "Close"
        self.CloseButton.PushButtonType = 2

        # inserts the control model into the dialog model
        self.DialogModel.insertByName("CloseButton", self.CloseButton)

        # add the action listener
        self.DialogContainer.getControl('CloseButton').addActionListener(self)
        self.DialogContainer.getControl('CloseButton').setActionCommand('CloseButton_OnClick')

        # --------- create an instance of Edit control, set properties ---
        self.DescriptionField = self.DialogModel.createInstance("com.sun.star.awt.UnoControlEditModel")

        self.DescriptionField.Name = "DescriptionField"
        self.DescriptionField.TabIndex = 3
        self.DescriptionField.PositionX = "112"
        self.DescriptionField.PositionY = "23"
        self.DescriptionField.Width = 128
        self.DescriptionField.Height = 126
        self.DescriptionField.MultiLine = True
        self.DescriptionField.AutoHScroll = True
        self.DescriptionField.AutoVScroll = True
        self.DescriptionField.ReadOnly = True
        self.DescriptionField.ContextWritingMode = False
        self.DescriptionField.Text = self.theme_description
        # self.DescriptionField.Text = "Hello World! this is description texts. Insert more texts here...\nLorem ipsum dolor sit amet, consectetur adipiscing elit. Maecenas luctus vitae sem ac rutrum. Nullam justo ligula, fringilla non ultricies.\nLorem ipsum dolor sit amet, consectetur adipiscing elit. Maecenas luctus vitae sem ac rutrum. Nullam justo ligula, fringilla non ultricies.\n\nauthor: libreoffice.id "

        # inserts the control model into the dialog model
        self.DialogModel.insertByName("DescriptionField", self.DescriptionField)

        # --------- create an instance of ImageControl control, set properties ---
        self.ImgThumb1 = self.DialogModel.createInstance("com.sun.star.awt.UnoControlImageControlModel")

        self.ImgThumb1.Name = "ImgThumb1"
        self.ImgThumb1.TabIndex = 4
        self.ImgThumb1.PositionX = "9"
        self.ImgThumb1.PositionY = "23"
        self.ImgThumb1.Width = 27
        self.ImgThumb1.Height = 24

        # inserts the control model into the dialog model
        self.DialogModel.insertByName("ImgThumb1", self.ImgThumb1)

        # --------- create an instance of ImageControl control, set properties ---
        self.ImgThumb2 = self.DialogModel.createInstance("com.sun.star.awt.UnoControlImageControlModel")

        self.ImgThumb2.Name = "ImgThumb2"
        self.ImgThumb2.TabIndex = 5
        self.ImgThumb2.PositionX = "42"
        self.ImgThumb2.PositionY = "23"
        self.ImgThumb2.Width = 27
        self.ImgThumb2.Height = 24

        # inserts the control model into the dialog model
        self.DialogModel.insertByName("ImgThumb2", self.ImgThumb2)

        # --------- create an instance of ImageControl control, set properties ---
        self.ImgThumb3 = self.DialogModel.createInstance("com.sun.star.awt.UnoControlImageControlModel")

        self.ImgThumb3.Name = "ImgThumb3"
        self.ImgThumb3.TabIndex = 6
        self.ImgThumb3.PositionX = "76"
        self.ImgThumb3.PositionY = "23"
        self.ImgThumb3.Width = 27
        self.ImgThumb3.Height = 24

        # inserts the control model into the dialog model
        self.DialogModel.insertByName("ImgThumb3", self.ImgThumb3)

        # --------- create an instance of ImageControl control, set properties ---
        self.ImgPreview = self.DialogModel.createInstance("com.sun.star.awt.UnoControlImageControlModel")

        self.ImgPreview.Name = "ImgPreview"
        self.ImgPreview.TabIndex = 7
        self.ImgPreview.PositionX = "9"
        self.ImgPreview.PositionY = "51"
        self.ImgPreview.Width = 94
        self.ImgPreview.Height = 98

        # inserts the control model into the dialog model
        self.DialogModel.insertByName("ImgPreview", self.ImgPreview)

        # --------- create an instance of FixedText control, set properties ---
        self.Label1 = self.DialogModel.createInstance("com.sun.star.awt.UnoControlFixedTextModel")

        self.Label1.Name = "Label1"
        self.Label1.TabIndex = 8
        self.Label1.PositionX = "9"
        self.Label1.PositionY = "3"
        self.Label1.Width = 230
        self.Label1.Height = 17
        self.Label1.Label = "Details for %s" % self.theme_name
        self.Label1.VerticalAlign = 1
        self.Label1.FontWeight = "800"
        # inserts the control model into the dialog model
        self.DialogModel.insertByName("Label1", self.Label1)

    # -----------------------------------------------------------
    #               Action events
    # -----------------------------------------------------------

    def actionPerformed(self, oActionEvent):

        if oActionEvent.ActionCommand == 'InstallButton_OnClick':
            self.InstallButton_OnClick()

        if oActionEvent.ActionCommand == 'RemoveButton_OnClick':
            self.RemoveButton_OnClick()

        if oActionEvent.ActionCommand == 'CloseButton_OnClick':
            self.CloseButton_OnClick()

# ----------------- END GENERATED CODE ----------------------------------------