# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './dlg_trj_edit_new.ui'
#
# Created: Wed Dec  7 12:55:07 2016
#      by: PyQt4 UI code generator 4.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_CDlgTrjEditNEW(object):
    def setupUi(self, CDlgTrjEditNEW):
        CDlgTrjEditNEW.setObjectName(_fromUtf8("CDlgTrjEditNEW"))
        CDlgTrjEditNEW.resize(464, 403)
        CDlgTrjEditNEW.setLocale(QtCore.QLocale(QtCore.QLocale.Portuguese, QtCore.QLocale.Brazil))
        CDlgTrjEditNEW.setSizeGripEnabled(True)
        CDlgTrjEditNEW.setModal(True)
        self.verticalLayout = QtGui.QVBoxLayout(CDlgTrjEditNEW)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.frmGrpID = QtGui.QFrame(CDlgTrjEditNEW)
        self.frmGrpID.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frmGrpID.setFrameShadow(QtGui.QFrame.Raised)
        self.frmGrpID.setObjectName(_fromUtf8("frmGrpID"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.frmGrpID)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.lblDesc = QtGui.QLabel(self.frmGrpID)
        self.lblDesc.setObjectName(_fromUtf8("lblDesc"))
        self.horizontalLayout.addWidget(self.lblDesc)
        self.qleDesc = QtGui.QLineEdit(self.frmGrpID)
        self.qleDesc.setCursorPosition(0)
        self.qleDesc.setObjectName(_fromUtf8("qleDesc"))
        self.horizontalLayout.addWidget(self.qleDesc)
        self.verticalLayout.addWidget(self.frmGrpID)
        self.frame_4 = QtGui.QFrame(CDlgTrjEditNEW)
        self.frame_4.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_4.setObjectName(_fromUtf8("frame_4"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.frame_4)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.gbxTrjPos = QtGui.QGroupBox(self.frame_4)
        self.gbxTrjPos.setObjectName(_fromUtf8("gbxTrjPos"))
        self.gridLayout_2 = QtGui.QGridLayout(self.gbxTrjPos)
        self.gridLayout_2.setMargin(3)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.cbxTCrd = QtGui.QComboBox(self.gbxTrjPos)
        self.cbxTCrd.setMinimumSize(QtCore.QSize(150, 0))
        self.cbxTCrd.setObjectName(_fromUtf8("cbxTCrd"))
        self.gridLayout_2.addWidget(self.cbxTCrd, 0, 0, 1, 1)
        self.stkCrd = QtGui.QStackedWidget(self.gbxTrjPos)
        self.stkCrd.setObjectName(_fromUtf8("stkCrd"))
        self.pagCart = QtGui.QWidget()
        self.pagCart.setObjectName(_fromUtf8("pagCart"))
        self.gridLayout_3 = QtGui.QGridLayout(self.pagCart)
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        self.lblCrd0 = QtGui.QLabel(self.pagCart)
        self.lblCrd0.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lblCrd0.setObjectName(_fromUtf8("lblCrd0"))
        self.gridLayout_3.addWidget(self.lblCrd0, 0, 0, 1, 1)
        self.lblCrd1 = QtGui.QLabel(self.pagCart)
        self.lblCrd1.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lblCrd1.setObjectName(_fromUtf8("lblCrd1"))
        self.gridLayout_3.addWidget(self.lblCrd1, 1, 0, 1, 1)
        self.lblCrd2 = QtGui.QLabel(self.pagCart)
        self.lblCrd2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lblCrd2.setObjectName(_fromUtf8("lblCrd2"))
        self.gridLayout_3.addWidget(self.lblCrd2, 2, 0, 1, 1)
        self.qsbX = QtGui.QDoubleSpinBox(self.pagCart)
        self.qsbX.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.qsbX.setDecimals(0)
        self.qsbX.setMinimum(-50000.0)
        self.qsbX.setMaximum(50000.0)
        self.qsbX.setSingleStep(100.0)
        self.qsbX.setObjectName(_fromUtf8("qsbX"))
        self.gridLayout_3.addWidget(self.qsbX, 0, 1, 1, 1)
        self.qsbY = QtGui.QDoubleSpinBox(self.pagCart)
        self.qsbY.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.qsbY.setDecimals(0)
        self.qsbY.setMinimum(-50000.0)
        self.qsbY.setMaximum(50000.0)
        self.qsbY.setSingleStep(100.0)
        self.qsbY.setObjectName(_fromUtf8("qsbY"))
        self.gridLayout_3.addWidget(self.qsbY, 1, 1, 1, 1)
        self.qsbZ = QtGui.QDoubleSpinBox(self.pagCart)
        self.qsbZ.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.qsbZ.setDecimals(0)
        self.qsbZ.setMinimum(0.0)
        self.qsbZ.setMaximum(80000.0)
        self.qsbZ.setSingleStep(100.0)
        self.qsbZ.setObjectName(_fromUtf8("qsbZ"))
        self.gridLayout_3.addWidget(self.qsbZ, 2, 1, 1, 1)
        self.stkCrd.addWidget(self.pagCart)
        self.pagPFix = QtGui.QWidget()
        self.pagPFix.setObjectName(_fromUtf8("pagPFix"))
        self.gridLayout_4 = QtGui.QGridLayout(self.pagPFix)
        self.gridLayout_4.setObjectName(_fromUtf8("gridLayout_4"))
        self.lblDist = QtGui.QLabel(self.pagPFix)
        self.lblDist.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lblDist.setObjectName(_fromUtf8("lblDist"))
        self.gridLayout_4.addWidget(self.lblDist, 0, 0, 1, 1)
        self.qsbDist = QtGui.QSpinBox(self.pagPFix)
        self.qsbDist.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.qsbDist.setMaximum(50000)
        self.qsbDist.setSingleStep(100)
        self.qsbDist.setObjectName(_fromUtf8("qsbDist"))
        self.gridLayout_4.addWidget(self.qsbDist, 0, 1, 1, 1)
        self.lblAzim = QtGui.QLabel(self.pagPFix)
        self.lblAzim.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lblAzim.setObjectName(_fromUtf8("lblAzim"))
        self.gridLayout_4.addWidget(self.lblAzim, 1, 0, 1, 1)
        self.qsbAzim = QtGui.QSpinBox(self.pagPFix)
        self.qsbAzim.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.qsbAzim.setMaximum(360)
        self.qsbAzim.setSingleStep(3)
        self.qsbAzim.setObjectName(_fromUtf8("qsbAzim"))
        self.gridLayout_4.addWidget(self.qsbAzim, 1, 1, 1, 1)
        self.lblFixo = QtGui.QLabel(self.pagPFix)
        self.lblFixo.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lblFixo.setObjectName(_fromUtf8("lblFixo"))
        self.gridLayout_4.addWidget(self.lblFixo, 2, 0, 1, 1)
        self.cbxFixo = QtGui.QComboBox(self.pagPFix)
        self.cbxFixo.setObjectName(_fromUtf8("cbxFixo"))
        self.gridLayout_4.addWidget(self.cbxFixo, 2, 1, 1, 1)
        self.stkCrd.addWidget(self.pagPFix)
        self.pagGeo = QtGui.QWidget()
        self.pagGeo.setObjectName(_fromUtf8("pagGeo"))
        self.gridLayout_5 = QtGui.QGridLayout(self.pagGeo)
        self.gridLayout_5.setObjectName(_fromUtf8("gridLayout_5"))
        self.lblLat = QtGui.QLabel(self.pagGeo)
        self.lblLat.setMinimumSize(QtCore.QSize(140, 0))
        self.lblLat.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lblLat.setObjectName(_fromUtf8("lblLat"))
        self.gridLayout_5.addWidget(self.lblLat, 0, 0, 1, 1)
        self.qleLat = QtGui.QLineEdit(self.pagGeo)
        self.qleLat.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.qleLat.setObjectName(_fromUtf8("qleLat"))
        self.gridLayout_5.addWidget(self.qleLat, 0, 1, 1, 1)
        self.lblLng = QtGui.QLabel(self.pagGeo)
        self.lblLng.setMinimumSize(QtCore.QSize(0, 0))
        self.lblLng.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lblLng.setObjectName(_fromUtf8("lblLng"))
        self.gridLayout_5.addWidget(self.lblLng, 1, 0, 1, 1)
        self.qleLng = QtGui.QLineEdit(self.pagGeo)
        self.qleLng.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.qleLng.setObjectName(_fromUtf8("qleLng"))
        self.gridLayout_5.addWidget(self.qleLng, 1, 1, 1, 1)
        self.lblAlt = QtGui.QLabel(self.pagGeo)
        self.lblAlt.setMinimumSize(QtCore.QSize(0, 0))
        self.lblAlt.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lblAlt.setObjectName(_fromUtf8("lblAlt"))
        self.gridLayout_5.addWidget(self.lblAlt, 2, 0, 1, 1)
        self.qsbAlt = QtGui.QSpinBox(self.pagGeo)
        self.qsbAlt.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.qsbAlt.setMaximum(80000)
        self.qsbAlt.setSingleStep(100)
        self.qsbAlt.setObjectName(_fromUtf8("qsbAlt"))
        self.gridLayout_5.addWidget(self.qsbAlt, 2, 1, 1, 1)
        self.stkCrd.addWidget(self.pagGeo)
        self.pagPol = QtGui.QWidget()
        self.pagPol.setObjectName(_fromUtf8("pagPol"))
        self.gridLayout_6 = QtGui.QGridLayout(self.pagPol)
        self.gridLayout_6.setObjectName(_fromUtf8("gridLayout_6"))
        self.lblDist_2 = QtGui.QLabel(self.pagPol)
        self.lblDist_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lblDist_2.setObjectName(_fromUtf8("lblDist_2"))
        self.gridLayout_6.addWidget(self.lblDist_2, 0, 0, 1, 1)
        self.lblAzim_2 = QtGui.QLabel(self.pagPol)
        self.lblAzim_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lblAzim_2.setObjectName(_fromUtf8("lblAzim_2"))
        self.gridLayout_6.addWidget(self.lblAzim_2, 1, 0, 1, 1)
        self.lblAlt_2 = QtGui.QLabel(self.pagPol)
        self.lblAlt_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lblAlt_2.setObjectName(_fromUtf8("lblAlt_2"))
        self.gridLayout_6.addWidget(self.lblAlt_2, 2, 0, 1, 1)
        self.qsbDist_2 = QtGui.QSpinBox(self.pagPol)
        self.qsbDist_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.qsbDist_2.setMaximum(50000)
        self.qsbDist_2.setSingleStep(100)
        self.qsbDist_2.setObjectName(_fromUtf8("qsbDist_2"))
        self.gridLayout_6.addWidget(self.qsbDist_2, 0, 1, 1, 1)
        self.qsbAzim_2 = QtGui.QSpinBox(self.pagPol)
        self.qsbAzim_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.qsbAzim_2.setMaximum(360)
        self.qsbAzim_2.setSingleStep(3)
        self.qsbAzim_2.setObjectName(_fromUtf8("qsbAzim_2"))
        self.gridLayout_6.addWidget(self.qsbAzim_2, 1, 1, 1, 1)
        self.qsbAlt_2 = QtGui.QSpinBox(self.pagPol)
        self.qsbAlt_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.qsbAlt_2.setMaximum(80000)
        self.qsbAlt_2.setSingleStep(100)
        self.qsbAlt_2.setObjectName(_fromUtf8("qsbAlt_2"))
        self.gridLayout_6.addWidget(self.qsbAlt_2, 2, 1, 1, 1)
        self.stkCrd.addWidget(self.pagPol)
        self.gridLayout_2.addWidget(self.stkCrd, 0, 1, 1, 1)
        self.horizontalLayout_2.addWidget(self.gbxTrjPos)
        self.verticalLayout.addWidget(self.frame_4)
        self.frame_8 = QtGui.QFrame(CDlgTrjEditNEW)
        self.frame_8.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_8.setObjectName(_fromUtf8("frame_8"))
        self.horizontalLayout_3 = QtGui.QHBoxLayout(self.frame_8)
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.groupBox = QtGui.QGroupBox(self.frame_8)
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.horizontalLayout_4 = QtGui.QHBoxLayout(self.groupBox)
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.qsbVel = QtGui.QSpinBox(self.groupBox)
        self.qsbVel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.qsbVel.setMaximum(1000)
        self.qsbVel.setSingleStep(10)
        self.qsbVel.setObjectName(_fromUtf8("qsbVel"))
        self.horizontalLayout_4.addWidget(self.qsbVel)
        self.horizontalLayout_3.addWidget(self.groupBox)
        self.groupBox_2 = QtGui.QGroupBox(self.frame_8)
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.horizontalLayout_11 = QtGui.QHBoxLayout(self.groupBox_2)
        self.horizontalLayout_11.setObjectName(_fromUtf8("horizontalLayout_11"))
        self.cbxPrc = QtGui.QComboBox(self.groupBox_2)
        self.cbxPrc.setObjectName(_fromUtf8("cbxPrc"))
        self.horizontalLayout_11.addWidget(self.cbxPrc)
        self.horizontalLayout_3.addWidget(self.groupBox_2)
        self.verticalLayout.addWidget(self.frame_8)
        self.widget = QtGui.QWidget(CDlgTrjEditNEW)
        self.widget.setObjectName(_fromUtf8("widget"))
        self.horizontalLayout_6 = QtGui.QHBoxLayout(self.widget)
        self.horizontalLayout_6.setMargin(0)
        self.horizontalLayout_6.setObjectName(_fromUtf8("horizontalLayout_6"))
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem)
        self.btnCancel = QtGui.QPushButton(self.widget)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/images/dbedit/stop.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnCancel.setIcon(icon)
        self.btnCancel.setObjectName(_fromUtf8("btnCancel"))
        self.horizontalLayout_6.addWidget(self.btnCancel)
        self.btnOk = QtGui.QPushButton(self.widget)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8(":/images/edit.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnOk.setIcon(icon1)
        self.btnOk.setObjectName(_fromUtf8("btnOk"))
        self.horizontalLayout_6.addWidget(self.btnOk)
        self.verticalLayout.addWidget(self.widget)
        self.lblDesc.setBuddy(self.qleDesc)
        self.lblCrd0.setBuddy(self.qsbX)
        self.lblCrd1.setBuddy(self.qsbY)
        self.lblCrd2.setBuddy(self.qsbZ)

        self.retranslateUi(CDlgTrjEditNEW)
        self.stkCrd.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(CDlgTrjEditNEW)
        CDlgTrjEditNEW.setTabOrder(self.qleDesc, self.cbxTCrd)
        CDlgTrjEditNEW.setTabOrder(self.cbxTCrd, self.qsbX)
        CDlgTrjEditNEW.setTabOrder(self.qsbX, self.qsbY)
        CDlgTrjEditNEW.setTabOrder(self.qsbY, self.qsbZ)
        CDlgTrjEditNEW.setTabOrder(self.qsbZ, self.qsbVel)
        CDlgTrjEditNEW.setTabOrder(self.qsbVel, self.cbxPrc)
        CDlgTrjEditNEW.setTabOrder(self.cbxPrc, self.btnCancel)
        CDlgTrjEditNEW.setTabOrder(self.btnCancel, self.btnOk)
        CDlgTrjEditNEW.setTabOrder(self.btnOk, self.qsbDist)
        CDlgTrjEditNEW.setTabOrder(self.qsbDist, self.qsbAzim)
        CDlgTrjEditNEW.setTabOrder(self.qsbAzim, self.cbxFixo)
        CDlgTrjEditNEW.setTabOrder(self.cbxFixo, self.qleLat)
        CDlgTrjEditNEW.setTabOrder(self.qleLat, self.qleLng)
        CDlgTrjEditNEW.setTabOrder(self.qleLng, self.qsbAlt)
        CDlgTrjEditNEW.setTabOrder(self.qsbAlt, self.qsbDist_2)
        CDlgTrjEditNEW.setTabOrder(self.qsbDist_2, self.qsbAzim_2)
        CDlgTrjEditNEW.setTabOrder(self.qsbAzim_2, self.qsbAlt_2)

    def retranslateUi(self, CDlgTrjEditNEW):
        CDlgTrjEditNEW.setWindowTitle(_translate("CDlgTrjEditNEW", "Edição de Trajetórias", None))
        self.lblDesc.setText(_translate("CDlgTrjEditNEW", "Descricão:", None))
        self.gbxTrjPos.setTitle(_translate("CDlgTrjEditNEW", "Posicão", None))
        self.lblCrd0.setText(_translate("CDlgTrjEditNEW", "X:", None))
        self.lblCrd1.setText(_translate("CDlgTrjEditNEW", "Y:", None))
        self.lblCrd2.setText(_translate("CDlgTrjEditNEW", "Z:", None))
        self.qsbX.setSuffix(_translate("CDlgTrjEditNEW", " m", None))
        self.qsbY.setSuffix(_translate("CDlgTrjEditNEW", " m", None))
        self.qsbZ.setSuffix(_translate("CDlgTrjEditNEW", " ft", None))
        self.lblDist.setText(_translate("CDlgTrjEditNEW", "Distância:", None))
        self.qsbDist.setSuffix(_translate("CDlgTrjEditNEW", " m", None))
        self.lblAzim.setText(_translate("CDlgTrjEditNEW", "Azimute:", None))
        self.qsbAzim.setSuffix(_translate("CDlgTrjEditNEW", " °", None))
        self.lblFixo.setText(_translate("CDlgTrjEditNEW", "Fixo:", None))
        self.lblLat.setText(_translate("CDlgTrjEditNEW", "Latitude:", None))
        self.lblLng.setText(_translate("CDlgTrjEditNEW", "Longitude:", None))
        self.lblAlt.setText(_translate("CDlgTrjEditNEW", "Altitude:", None))
        self.qsbAlt.setSuffix(_translate("CDlgTrjEditNEW", " ft", None))
        self.lblDist_2.setText(_translate("CDlgTrjEditNEW", "Distância:", None))
        self.lblAzim_2.setText(_translate("CDlgTrjEditNEW", "Azimute:", None))
        self.lblAlt_2.setText(_translate("CDlgTrjEditNEW", "Altitude:", None))
        self.qsbDist_2.setSuffix(_translate("CDlgTrjEditNEW", " m", None))
        self.qsbAzim_2.setSuffix(_translate("CDlgTrjEditNEW", " °", None))
        self.qsbAlt_2.setSuffix(_translate("CDlgTrjEditNEW", " ft", None))
        self.groupBox.setTitle(_translate("CDlgTrjEditNEW", "Velocidade", None))
        self.qsbVel.setSuffix(_translate("CDlgTrjEditNEW", " kt", None))
        self.groupBox_2.setTitle(_translate("CDlgTrjEditNEW", "Procedimento", None))
        self.btnCancel.setText(_translate("CDlgTrjEditNEW", "Cancela", None))
        self.btnOk.setText(_translate("CDlgTrjEditNEW", "Ok", None))

import resources_rc