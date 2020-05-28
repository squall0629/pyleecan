# -*- coding: utf-8 -*-

# File generated according to SMachineDimension.ui
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_SMachineDimension(object):
    def setupUi(self, SMachineDimension):
        SMachineDimension.setObjectName("SMachineDimension")
        SMachineDimension.resize(650, 550)
        SMachineDimension.setMinimumSize(QtCore.QSize(650, 550))
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(SMachineDimension)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.img_machine = QtWidgets.QLabel(SMachineDimension)
        self.img_machine.setMinimumSize(QtCore.QSize(400, 400))
        self.img_machine.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.img_machine.setText("")
        self.img_machine.setPixmap(
            QtGui.QPixmap(":/images/images/MachineSetup/MachineDimension/Dim_IRS.png")
        )
        self.img_machine.setScaledContents(True)
        self.img_machine.setObjectName("img_machine")
        self.horizontalLayout_2.addWidget(self.img_machine)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.g_stator = QtWidgets.QGroupBox(SMachineDimension)
        self.g_stator.setMinimumSize(QtCore.QSize(150, 0))
        self.g_stator.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.g_stator.setObjectName("g_stator")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.g_stator)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.in_SRext = QtWidgets.QLabel(self.g_stator)
        self.in_SRext.setMinimumSize(QtCore.QSize(30, 0))
        self.in_SRext.setObjectName("in_SRext")
        self.gridLayout_2.addWidget(self.in_SRext, 0, 0, 1, 1)
        self.lf_SRext = FloatEdit(self.g_stator)
        self.lf_SRext.setMaximumSize(QtCore.QSize(100, 16777215))
        self.lf_SRext.setObjectName("lf_SRext")
        self.gridLayout_2.addWidget(self.lf_SRext, 0, 1, 1, 1)
        self.unit_SRext = QtWidgets.QLabel(self.g_stator)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.unit_SRext.sizePolicy().hasHeightForWidth())
        self.unit_SRext.setSizePolicy(sizePolicy)
        self.unit_SRext.setObjectName("unit_SRext")
        self.gridLayout_2.addWidget(self.unit_SRext, 0, 2, 1, 1)
        self.in_SRint = QtWidgets.QLabel(self.g_stator)
        self.in_SRint.setMinimumSize(QtCore.QSize(30, 0))
        self.in_SRint.setObjectName("in_SRint")
        self.gridLayout_2.addWidget(self.in_SRint, 1, 0, 1, 1)
        self.lf_SRint = FloatEdit(self.g_stator)
        self.lf_SRint.setMaximumSize(QtCore.QSize(100, 100))
        self.lf_SRint.setObjectName("lf_SRint")
        self.gridLayout_2.addWidget(self.lf_SRint, 1, 1, 1, 1)
        self.unit_SRint = QtWidgets.QLabel(self.g_stator)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.unit_SRint.sizePolicy().hasHeightForWidth())
        self.unit_SRint.setSizePolicy(sizePolicy)
        self.unit_SRint.setObjectName("unit_SRint")
        self.gridLayout_2.addWidget(self.unit_SRint, 1, 2, 1, 1)
        self.verticalLayout.addWidget(self.g_stator)
        self.g_rotor = QtWidgets.QGroupBox(SMachineDimension)
        self.g_rotor.setObjectName("g_rotor")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.g_rotor)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.in_RRext = QtWidgets.QLabel(self.g_rotor)
        self.in_RRext.setMinimumSize(QtCore.QSize(30, 0))
        self.in_RRext.setObjectName("in_RRext")
        self.gridLayout_3.addWidget(self.in_RRext, 0, 0, 1, 1)
        self.lf_RRext = FloatEdit(self.g_rotor)
        self.lf_RRext.setMaximumSize(QtCore.QSize(100, 16777215))
        self.lf_RRext.setObjectName("lf_RRext")
        self.gridLayout_3.addWidget(self.lf_RRext, 0, 1, 1, 1)
        self.unit_RRext = QtWidgets.QLabel(self.g_rotor)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.unit_RRext.sizePolicy().hasHeightForWidth())
        self.unit_RRext.setSizePolicy(sizePolicy)
        self.unit_RRext.setObjectName("unit_RRext")
        self.gridLayout_3.addWidget(self.unit_RRext, 0, 2, 1, 1)
        self.in_RRint = QtWidgets.QLabel(self.g_rotor)
        self.in_RRint.setMinimumSize(QtCore.QSize(30, 0))
        self.in_RRint.setObjectName("in_RRint")
        self.gridLayout_3.addWidget(self.in_RRint, 1, 0, 1, 1)
        self.lf_RRint = FloatEdit(self.g_rotor)
        self.lf_RRint.setMaximumSize(QtCore.QSize(100, 100))
        self.lf_RRint.setObjectName("lf_RRint")
        self.gridLayout_3.addWidget(self.lf_RRint, 1, 1, 1, 1)
        self.unit_RRint = QtWidgets.QLabel(self.g_rotor)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.unit_RRint.sizePolicy().hasHeightForWidth())
        self.unit_RRint.setSizePolicy(sizePolicy)
        self.unit_RRint.setObjectName("unit_RRint")
        self.gridLayout_3.addWidget(self.unit_RRint, 1, 2, 1, 1)
        self.verticalLayout.addWidget(self.g_rotor)
        self.out_airgap = QtWidgets.QLabel(SMachineDimension)
        self.out_airgap.setObjectName("out_airgap")
        self.verticalLayout.addWidget(self.out_airgap)
        self.g_shaft = QtWidgets.QGroupBox(SMachineDimension)
        self.g_shaft.setMinimumSize(QtCore.QSize(0, 0))
        self.g_shaft.setCheckable(True)
        self.g_shaft.setObjectName("g_shaft")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.g_shaft)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.out_Drsh = QtWidgets.QLabel(self.g_shaft)
        self.out_Drsh.setObjectName("out_Drsh")
        self.horizontalLayout_5.addWidget(self.out_Drsh)
        self.verticalLayout.addWidget(self.g_shaft)
        self.g_frame = QtWidgets.QGroupBox(SMachineDimension)
        self.g_frame.setCheckable(True)
        self.g_frame.setObjectName("g_frame")
        self.gridLayout = QtWidgets.QGridLayout(self.g_frame)
        self.gridLayout.setObjectName("gridLayout")
        self.in_Wfra = QtWidgets.QLabel(self.g_frame)
        self.in_Wfra.setObjectName("in_Wfra")
        self.gridLayout.addWidget(self.in_Wfra, 0, 0, 1, 1)
        self.lf_Wfra = FloatEdit(self.g_frame)
        self.lf_Wfra.setMaximumSize(QtCore.QSize(100, 16777215))
        self.lf_Wfra.setObjectName("lf_Wfra")
        self.gridLayout.addWidget(self.lf_Wfra, 0, 1, 1, 1)
        self.unit_Wfra = QtWidgets.QLabel(self.g_frame)
        self.unit_Wfra.setObjectName("unit_Wfra")
        self.gridLayout.addWidget(self.unit_Wfra, 0, 2, 1, 1)
        self.in_Lfra = QtWidgets.QLabel(self.g_frame)
        self.in_Lfra.setObjectName("in_Lfra")
        self.gridLayout.addWidget(self.in_Lfra, 1, 0, 1, 1)
        self.lf_Lfra = FloatEdit(self.g_frame)
        self.lf_Lfra.setMaximumSize(QtCore.QSize(100, 16777215))
        self.lf_Lfra.setObjectName("lf_Lfra")
        self.gridLayout.addWidget(self.lf_Lfra, 1, 1, 1, 1)
        self.unit_Lfra = QtWidgets.QLabel(self.g_frame)
        self.unit_Lfra.setObjectName("unit_Lfra")
        self.gridLayout.addWidget(self.unit_Lfra, 1, 2, 1, 1)
        self.verticalLayout.addWidget(self.g_frame)
        spacerItem = QtWidgets.QSpacerItem(
            20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding
        )
        self.verticalLayout.addItem(spacerItem)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem1 = QtWidgets.QSpacerItem(
            40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum
        )
        self.horizontalLayout.addItem(spacerItem1)
        self.b_previous = QtWidgets.QPushButton(SMachineDimension)
        self.b_previous.setObjectName("b_previous")
        self.horizontalLayout.addWidget(self.b_previous)
        self.b_next = QtWidgets.QPushButton(SMachineDimension)
        self.b_next.setObjectName("b_next")
        self.horizontalLayout.addWidget(self.b_next)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2.addLayout(self.verticalLayout)

        self.retranslateUi(SMachineDimension)
        self.g_shaft.toggled["bool"].connect(self.out_Drsh.setVisible)
        self.g_frame.toggled["bool"].connect(self.in_Lfra.setVisible)
        self.g_frame.toggled["bool"].connect(self.unit_Lfra.setVisible)
        QtCore.QMetaObject.connectSlotsByName(SMachineDimension)

    def retranslateUi(self, SMachineDimension):
        _translate = QtCore.QCoreApplication.translate
        SMachineDimension.setWindowTitle(_translate("SMachineDimension", "Form"))
        self.g_stator.setTitle(_translate("SMachineDimension", "Stator"))
        self.in_SRext.setToolTip(
            _translate("SMachineDimension", "Stator external radius")
        )
        self.in_SRext.setText(_translate("SMachineDimension", "Rext:"))
        self.lf_SRext.setToolTip(
            _translate("SMachineDimension", "Stator external radius")
        )
        self.unit_SRext.setText(_translate("SMachineDimension", "m"))
        self.in_SRint.setToolTip(
            _translate("SMachineDimension", "Stator internal radius")
        )
        self.in_SRint.setText(_translate("SMachineDimension", "Rint:"))
        self.lf_SRint.setToolTip(
            _translate("SMachineDimension", "Stator internal radius")
        )
        self.unit_SRint.setText(_translate("SMachineDimension", "m"))
        self.g_rotor.setTitle(_translate("SMachineDimension", "Rotor"))
        self.in_RRext.setToolTip(
            _translate("SMachineDimension", "Rotor external radius")
        )
        self.in_RRext.setText(_translate("SMachineDimension", "Rext:"))
        self.lf_RRext.setToolTip(
            _translate("SMachineDimension", "Rotor external radius")
        )
        self.unit_RRext.setText(_translate("SMachineDimension", "m"))
        self.in_RRint.setToolTip(
            _translate("SMachineDimension", "Rotor internal radius")
        )
        self.in_RRint.setText(_translate("SMachineDimension", "Rint:"))
        self.lf_RRint.setToolTip(
            _translate("SMachineDimension", "Rotor internal radius")
        )
        self.unit_RRint.setText(_translate("SMachineDimension", "m"))
        self.out_airgap.setToolTip(
            _translate(
                "SMachineDimension",
                "mechanical airgap width (distance between stator bore and rotor bore radii)",
            )
        )
        self.out_airgap.setText(_translate("SMachineDimension", "airgap = "))
        self.g_shaft.setTitle(_translate("SMachineDimension", "Shaft"))
        self.out_Drsh.setToolTip(_translate("SMachineDimension", "Shaft Diameter"))
        self.out_Drsh.setText(_translate("SMachineDimension", "Drsh = 2*Rotor.Rint"))
        self.g_frame.setTitle(_translate("SMachineDimension", "Frame"))
        self.in_Wfra.setToolTip(_translate("SMachineDimension", "Frame width"))
        self.in_Wfra.setWhatsThis(_translate("SMachineDimension", "Frame width"))
        self.in_Wfra.setText(_translate("SMachineDimension", "Wfra:"))
        self.lf_Wfra.setToolTip(_translate("SMachineDimension", "Frame width"))
        self.lf_Wfra.setWhatsThis(_translate("SMachineDimension", "Frame width"))
        self.unit_Wfra.setToolTip(_translate("SMachineDimension", "Frame width"))
        self.unit_Wfra.setWhatsThis(_translate("SMachineDimension", "Frame width"))
        self.unit_Wfra.setText(_translate("SMachineDimension", "m"))
        self.in_Lfra.setToolTip(_translate("SMachineDimension", "Frame length"))
        self.in_Lfra.setWhatsThis(_translate("SMachineDimension", "Frame length"))
        self.in_Lfra.setText(_translate("SMachineDimension", "Lfra:"))
        self.lf_Lfra.setToolTip(_translate("SMachineDimension", "Frame length"))
        self.lf_Lfra.setWhatsThis(_translate("SMachineDimension", "Frame length"))
        self.unit_Lfra.setToolTip(_translate("SMachineDimension", "Frame length"))
        self.unit_Lfra.setWhatsThis(_translate("SMachineDimension", "Frame length"))
        self.unit_Lfra.setText(_translate("SMachineDimension", "m"))
        self.b_previous.setText(_translate("SMachineDimension", "Previous"))
        self.b_next.setText(_translate("SMachineDimension", "Next"))


from .....GUI.Tools.FloatEdit import FloatEdit
from pyleecan.GUI.Resources import pyleecan_rc
