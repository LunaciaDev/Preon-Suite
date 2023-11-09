# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'weatherWindow.ui'
##
## Created by: Qt User Interface Compiler version 6.5.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QGridLayout, QHBoxLayout, QLabel,
    QSizePolicy, QSpacerItem, QToolButton, QVBoxLayout,
    QWidget)

class Ui_weatherWindow(object):
    def setupUi(self, weatherWindow):
        if not weatherWindow.objectName():
            weatherWindow.setObjectName(u"weatherWindow")
        weatherWindow.resize(1080, 720)
        self.verticalLayout_2 = QVBoxLayout(weatherWindow)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalSpacer_2 = QSpacerItem(20, 15, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout_2.addItem(self.verticalSpacer_2)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.MinimumExpanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_4)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.cityLabel = QLabel(weatherWindow)
        self.cityLabel.setObjectName(u"cityLabel")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cityLabel.sizePolicy().hasHeightForWidth())
        self.cityLabel.setSizePolicy(sizePolicy)
        self.cityLabel.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.cityLabel)

        self.temperatureLabel = QLabel(weatherWindow)
        self.temperatureLabel.setObjectName(u"temperatureLabel")
        self.temperatureLabel.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.temperatureLabel)

        self.perceivedTempLabel = QLabel(weatherWindow)
        self.perceivedTempLabel.setObjectName(u"perceivedTempLabel")
        sizePolicy.setHeightForWidth(self.perceivedTempLabel.sizePolicy().hasHeightForWidth())
        self.perceivedTempLabel.setSizePolicy(sizePolicy)
        self.perceivedTempLabel.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.perceivedTempLabel)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.weatherTypeLabel = QLabel(weatherWindow)
        self.weatherTypeLabel.setObjectName(u"weatherTypeLabel")
        self.weatherTypeLabel.setMaximumSize(QSize(16777215, 30))
        self.weatherTypeLabel.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.weatherTypeLabel, 0, 0, 1, 1)

        self.minMaxTempLabel = QLabel(weatherWindow)
        self.minMaxTempLabel.setObjectName(u"minMaxTempLabel")
        self.minMaxTempLabel.setMaximumSize(QSize(16777215, 30))
        self.minMaxTempLabel.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.minMaxTempLabel, 1, 0, 1, 1)

        self.humidityLabel = QLabel(weatherWindow)
        self.humidityLabel.setObjectName(u"humidityLabel")
        self.humidityLabel.setMaximumSize(QSize(16777215, 30))
        self.humidityLabel.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.humidityLabel, 0, 1, 1, 1)

        self.windSpeedLabel = QLabel(weatherWindow)
        self.windSpeedLabel.setObjectName(u"windSpeedLabel")
        self.windSpeedLabel.setMaximumSize(QSize(16777215, 30))
        self.windSpeedLabel.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.windSpeedLabel, 1, 1, 1, 1)


        self.verticalLayout.addLayout(self.gridLayout)


        self.horizontalLayout.addLayout(self.verticalLayout)

        self.horizontalSpacer_3 = QSpacerItem(80, 20, QSizePolicy.Preferred, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_3)

        self.weatherIcon = QLabel(weatherWindow)
        self.weatherIcon.setObjectName(u"weatherIcon")
        self.weatherIcon.setMinimumSize(QSize(120, 120))
        self.weatherIcon.setScaledContents(False)

        self.horizontalLayout.addWidget(self.weatherIcon)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.MinimumExpanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_5)


        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.verticalSpacer = QSpacerItem(20, 15, QSizePolicy.Minimum, QSizePolicy.Maximum)

        self.verticalLayout_2.addItem(self.verticalSpacer)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setSpacing(15)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(15, -1, 15, -1)
        self.forecast_1 = QWidget(weatherWindow)
        self.forecast_1.setObjectName(u"forecast_1")
        self.verticalLayout_6 = QVBoxLayout(self.forecast_1)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 6, 0, 6)
        self.forecastDateLabel_1 = QLabel(self.forecast_1)
        self.forecastDateLabel_1.setObjectName(u"forecastDateLabel_1")
        self.forecastDateLabel_1.setMaximumSize(QSize(16777215, 30))
        self.forecastDateLabel_1.setAlignment(Qt.AlignCenter)

        self.verticalLayout_6.addWidget(self.forecastDateLabel_1)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Preferred, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_6)

        self.forecastWeatherIcon_1 = QLabel(self.forecast_1)
        self.forecastWeatherIcon_1.setObjectName(u"forecastWeatherIcon_1")
        self.forecastWeatherIcon_1.setMinimumSize(QSize(90, 90))
        self.forecastWeatherIcon_1.setMaximumSize(QSize(120, 120))
        self.forecastWeatherIcon_1.setScaledContents(False)
        self.forecastWeatherIcon_1.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_4.addWidget(self.forecastWeatherIcon_1)

        self.horizontalSpacer_7 = QSpacerItem(40, 20, QSizePolicy.Preferred, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_7)


        self.verticalLayout_6.addLayout(self.horizontalLayout_4)

        self.forecastTempLabel_1 = QLabel(self.forecast_1)
        self.forecastTempLabel_1.setObjectName(u"forecastTempLabel_1")
        self.forecastTempLabel_1.setMaximumSize(QSize(16777215, 30))
        self.forecastTempLabel_1.setAlignment(Qt.AlignCenter)

        self.verticalLayout_6.addWidget(self.forecastTempLabel_1)

        self.forecastPerceivedLabel_1 = QLabel(self.forecast_1)
        self.forecastPerceivedLabel_1.setObjectName(u"forecastPerceivedLabel_1")
        self.forecastPerceivedLabel_1.setMaximumSize(QSize(16777215, 30))
        self.forecastPerceivedLabel_1.setAlignment(Qt.AlignCenter)
        self.forecastPerceivedLabel_1.setWordWrap(True)

        self.verticalLayout_6.addWidget(self.forecastPerceivedLabel_1)

        self.forecastHighLowTempLabel_1 = QLabel(self.forecast_1)
        self.forecastHighLowTempLabel_1.setObjectName(u"forecastHighLowTempLabel_1")
        self.forecastHighLowTempLabel_1.setMaximumSize(QSize(16777215, 30))
        self.forecastHighLowTempLabel_1.setAlignment(Qt.AlignCenter)

        self.verticalLayout_6.addWidget(self.forecastHighLowTempLabel_1)


        self.horizontalLayout_3.addWidget(self.forecast_1)

        self.forecast_2 = QWidget(weatherWindow)
        self.forecast_2.setObjectName(u"forecast_2")
        self.verticalLayout_8 = QVBoxLayout(self.forecast_2)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 6, 0, 6)
        self.forecastDateLabel_2 = QLabel(self.forecast_2)
        self.forecastDateLabel_2.setObjectName(u"forecastDateLabel_2")
        self.forecastDateLabel_2.setMaximumSize(QSize(16777215, 30))
        self.forecastDateLabel_2.setAlignment(Qt.AlignCenter)

        self.verticalLayout_8.addWidget(self.forecastDateLabel_2)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalSpacer_10 = QSpacerItem(40, 20, QSizePolicy.Preferred, QSizePolicy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_10)

        self.forecastWeatherIcon_2 = QLabel(self.forecast_2)
        self.forecastWeatherIcon_2.setObjectName(u"forecastWeatherIcon_2")
        self.forecastWeatherIcon_2.setMinimumSize(QSize(90, 90))
        self.forecastWeatherIcon_2.setMaximumSize(QSize(120, 120))
        self.forecastWeatherIcon_2.setScaledContents(False)
        self.forecastWeatherIcon_2.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_6.addWidget(self.forecastWeatherIcon_2)

        self.horizontalSpacer_11 = QSpacerItem(40, 20, QSizePolicy.Preferred, QSizePolicy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_11)


        self.verticalLayout_8.addLayout(self.horizontalLayout_6)

        self.forecastTempLabel_2 = QLabel(self.forecast_2)
        self.forecastTempLabel_2.setObjectName(u"forecastTempLabel_2")
        self.forecastTempLabel_2.setMaximumSize(QSize(16777215, 30))
        self.forecastTempLabel_2.setAlignment(Qt.AlignCenter)

        self.verticalLayout_8.addWidget(self.forecastTempLabel_2)

        self.forecastPerceivedLabel_2 = QLabel(self.forecast_2)
        self.forecastPerceivedLabel_2.setObjectName(u"forecastPerceivedLabel_2")
        self.forecastPerceivedLabel_2.setMaximumSize(QSize(16777215, 30))
        self.forecastPerceivedLabel_2.setAlignment(Qt.AlignCenter)
        self.forecastPerceivedLabel_2.setWordWrap(True)

        self.verticalLayout_8.addWidget(self.forecastPerceivedLabel_2)

        self.forecastHighLowTempLabel_2 = QLabel(self.forecast_2)
        self.forecastHighLowTempLabel_2.setObjectName(u"forecastHighLowTempLabel_2")
        self.forecastHighLowTempLabel_2.setMaximumSize(QSize(16777215, 30))
        self.forecastHighLowTempLabel_2.setAlignment(Qt.AlignCenter)

        self.verticalLayout_8.addWidget(self.forecastHighLowTempLabel_2)


        self.horizontalLayout_3.addWidget(self.forecast_2)

        self.forecast_3 = QWidget(weatherWindow)
        self.forecast_3.setObjectName(u"forecast_3")
        self.verticalLayout_9 = QVBoxLayout(self.forecast_3)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(0, 6, 0, 6)
        self.forecastDateLabel_3 = QLabel(self.forecast_3)
        self.forecastDateLabel_3.setObjectName(u"forecastDateLabel_3")
        self.forecastDateLabel_3.setMaximumSize(QSize(16777215, 30))
        self.forecastDateLabel_3.setAlignment(Qt.AlignCenter)

        self.verticalLayout_9.addWidget(self.forecastDateLabel_3)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalSpacer_12 = QSpacerItem(40, 20, QSizePolicy.Preferred, QSizePolicy.Minimum)

        self.horizontalLayout_7.addItem(self.horizontalSpacer_12)

        self.forecastWeatherIcon_3 = QLabel(self.forecast_3)
        self.forecastWeatherIcon_3.setObjectName(u"forecastWeatherIcon_3")
        self.forecastWeatherIcon_3.setMinimumSize(QSize(90, 90))
        self.forecastWeatherIcon_3.setMaximumSize(QSize(120, 120))
        self.forecastWeatherIcon_3.setScaledContents(False)
        self.forecastWeatherIcon_3.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_7.addWidget(self.forecastWeatherIcon_3)

        self.horizontalSpacer_13 = QSpacerItem(40, 20, QSizePolicy.Preferred, QSizePolicy.Minimum)

        self.horizontalLayout_7.addItem(self.horizontalSpacer_13)


        self.verticalLayout_9.addLayout(self.horizontalLayout_7)

        self.forecastTempLabel_3 = QLabel(self.forecast_3)
        self.forecastTempLabel_3.setObjectName(u"forecastTempLabel_3")
        self.forecastTempLabel_3.setMaximumSize(QSize(16777215, 30))
        self.forecastTempLabel_3.setAlignment(Qt.AlignCenter)

        self.verticalLayout_9.addWidget(self.forecastTempLabel_3)

        self.forecastPerceivedLabel_3 = QLabel(self.forecast_3)
        self.forecastPerceivedLabel_3.setObjectName(u"forecastPerceivedLabel_3")
        self.forecastPerceivedLabel_3.setMaximumSize(QSize(16777215, 30))
        self.forecastPerceivedLabel_3.setAlignment(Qt.AlignCenter)
        self.forecastPerceivedLabel_3.setWordWrap(True)

        self.verticalLayout_9.addWidget(self.forecastPerceivedLabel_3)

        self.forecastHighLowTempLabel_3 = QLabel(self.forecast_3)
        self.forecastHighLowTempLabel_3.setObjectName(u"forecastHighLowTempLabel_3")
        self.forecastHighLowTempLabel_3.setMaximumSize(QSize(16777215, 30))
        self.forecastHighLowTempLabel_3.setAlignment(Qt.AlignCenter)

        self.verticalLayout_9.addWidget(self.forecastHighLowTempLabel_3)


        self.horizontalLayout_3.addWidget(self.forecast_3)

        self.forecast_4 = QWidget(weatherWindow)
        self.forecast_4.setObjectName(u"forecast_4")
        self.verticalLayout_10 = QVBoxLayout(self.forecast_4)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(0, 6, 0, 6)
        self.forecastDateLabel_4 = QLabel(self.forecast_4)
        self.forecastDateLabel_4.setObjectName(u"forecastDateLabel_4")
        self.forecastDateLabel_4.setMaximumSize(QSize(16777215, 30))
        self.forecastDateLabel_4.setAlignment(Qt.AlignCenter)

        self.verticalLayout_10.addWidget(self.forecastDateLabel_4)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalSpacer_14 = QSpacerItem(40, 20, QSizePolicy.Preferred, QSizePolicy.Minimum)

        self.horizontalLayout_8.addItem(self.horizontalSpacer_14)

        self.forecastWeatherIcon_4 = QLabel(self.forecast_4)
        self.forecastWeatherIcon_4.setObjectName(u"forecastWeatherIcon_4")
        self.forecastWeatherIcon_4.setMinimumSize(QSize(90, 90))
        self.forecastWeatherIcon_4.setMaximumSize(QSize(120, 120))
        self.forecastWeatherIcon_4.setScaledContents(False)
        self.forecastWeatherIcon_4.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_8.addWidget(self.forecastWeatherIcon_4)

        self.horizontalSpacer_15 = QSpacerItem(40, 20, QSizePolicy.Preferred, QSizePolicy.Minimum)

        self.horizontalLayout_8.addItem(self.horizontalSpacer_15)


        self.verticalLayout_10.addLayout(self.horizontalLayout_8)

        self.forecastTempLabel_4 = QLabel(self.forecast_4)
        self.forecastTempLabel_4.setObjectName(u"forecastTempLabel_4")
        self.forecastTempLabel_4.setMaximumSize(QSize(16777215, 30))
        self.forecastTempLabel_4.setAlignment(Qt.AlignCenter)

        self.verticalLayout_10.addWidget(self.forecastTempLabel_4)

        self.forecastPerceivedLabel_4 = QLabel(self.forecast_4)
        self.forecastPerceivedLabel_4.setObjectName(u"forecastPerceivedLabel_4")
        self.forecastPerceivedLabel_4.setMaximumSize(QSize(16777215, 30))
        self.forecastPerceivedLabel_4.setAlignment(Qt.AlignCenter)
        self.forecastPerceivedLabel_4.setWordWrap(True)

        self.verticalLayout_10.addWidget(self.forecastPerceivedLabel_4)

        self.forecastHighLowTempLabel_4 = QLabel(self.forecast_4)
        self.forecastHighLowTempLabel_4.setObjectName(u"forecastHighLowTempLabel_4")
        self.forecastHighLowTempLabel_4.setMaximumSize(QSize(16777215, 30))
        self.forecastHighLowTempLabel_4.setAlignment(Qt.AlignCenter)

        self.verticalLayout_10.addWidget(self.forecastHighLowTempLabel_4)


        self.horizontalLayout_3.addWidget(self.forecast_4)

        self.forecast_5 = QWidget(weatherWindow)
        self.forecast_5.setObjectName(u"forecast_5")
        self.verticalLayout_11 = QVBoxLayout(self.forecast_5)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(0, 6, 0, 6)
        self.forecastDateLabel_5 = QLabel(self.forecast_5)
        self.forecastDateLabel_5.setObjectName(u"forecastDateLabel_5")
        self.forecastDateLabel_5.setMaximumSize(QSize(16777215, 30))
        self.forecastDateLabel_5.setAlignment(Qt.AlignCenter)

        self.verticalLayout_11.addWidget(self.forecastDateLabel_5)

        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalSpacer_16 = QSpacerItem(40, 20, QSizePolicy.Preferred, QSizePolicy.Minimum)

        self.horizontalLayout_9.addItem(self.horizontalSpacer_16)

        self.forecastWeatherIcon_5 = QLabel(self.forecast_5)
        self.forecastWeatherIcon_5.setObjectName(u"forecastWeatherIcon_5")
        self.forecastWeatherIcon_5.setMinimumSize(QSize(90, 90))
        self.forecastWeatherIcon_5.setMaximumSize(QSize(120, 120))
        self.forecastWeatherIcon_5.setScaledContents(False)
        self.forecastWeatherIcon_5.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_9.addWidget(self.forecastWeatherIcon_5)

        self.horizontalSpacer_17 = QSpacerItem(40, 20, QSizePolicy.Preferred, QSizePolicy.Minimum)

        self.horizontalLayout_9.addItem(self.horizontalSpacer_17)


        self.verticalLayout_11.addLayout(self.horizontalLayout_9)

        self.forecastTempLabel_5 = QLabel(self.forecast_5)
        self.forecastTempLabel_5.setObjectName(u"forecastTempLabel_5")
        self.forecastTempLabel_5.setMaximumSize(QSize(16777215, 30))
        self.forecastTempLabel_5.setAlignment(Qt.AlignCenter)

        self.verticalLayout_11.addWidget(self.forecastTempLabel_5)

        self.forecastPerceivedLabel_5 = QLabel(self.forecast_5)
        self.forecastPerceivedLabel_5.setObjectName(u"forecastPerceivedLabel_5")
        self.forecastPerceivedLabel_5.setMaximumSize(QSize(16777215, 30))
        self.forecastPerceivedLabel_5.setAlignment(Qt.AlignCenter)
        self.forecastPerceivedLabel_5.setWordWrap(True)

        self.verticalLayout_11.addWidget(self.forecastPerceivedLabel_5)

        self.forecastHighLowTempLabel_5 = QLabel(self.forecast_5)
        self.forecastHighLowTempLabel_5.setObjectName(u"forecastHighLowTempLabel_5")
        self.forecastHighLowTempLabel_5.setMaximumSize(QSize(16777215, 30))
        self.forecastHighLowTempLabel_5.setAlignment(Qt.AlignCenter)

        self.verticalLayout_11.addWidget(self.forecastHighLowTempLabel_5)


        self.horizontalLayout_3.addWidget(self.forecast_5)


        self.verticalLayout_2.addLayout(self.horizontalLayout_3)

        self.widget_6 = QWidget(weatherWindow)
        self.widget_6.setObjectName(u"widget_6")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Minimum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.widget_6.sizePolicy().hasHeightForWidth())
        self.widget_6.setSizePolicy(sizePolicy1)
        self.widget_6.setMaximumSize(QSize(16777215, 50))
        self.horizontalLayout_2 = QHBoxLayout(self.widget_6)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer = QSpacerItem(1, 17, QSizePolicy.MinimumExpanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.assistantButton = QToolButton(self.widget_6)
        self.assistantButton.setObjectName(u"assistantButton")

        self.horizontalLayout_2.addWidget(self.assistantButton)

        self.horizontalSpacer_2 = QSpacerItem(1, 20, QSizePolicy.MinimumExpanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)

        self.creditLabel = QLabel(self.widget_6)
        self.creditLabel.setObjectName(u"creditLabel")
        self.creditLabel.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.creditLabel.setOpenExternalLinks(True)
        self.creditLabel.setTextInteractionFlags(Qt.NoTextInteraction)

        self.horizontalLayout_2.addWidget(self.creditLabel)

        self.openWeatherIcon = QToolButton(self.widget_6)
        self.openWeatherIcon.setObjectName(u"openWeatherIcon")

        self.horizontalLayout_2.addWidget(self.openWeatherIcon)


        self.verticalLayout_2.addWidget(self.widget_6)


        self.retranslateUi(weatherWindow)

        QMetaObject.connectSlotsByName(weatherWindow)
    # setupUi

    def retranslateUi(self, weatherWindow):
        weatherWindow.setWindowTitle(QCoreApplication.translate("weatherWindow", u"Form", None))
        self.cityLabel.setText(QCoreApplication.translate("weatherWindow", u"Binh Duong", None))
        self.temperatureLabel.setText(QCoreApplication.translate("weatherWindow", u"28C", None))
        self.perceivedTempLabel.setText(QCoreApplication.translate("weatherWindow", u"Feel like 31C", None))
        self.weatherTypeLabel.setText(QCoreApplication.translate("weatherWindow", u"Mostly Cloudy", None))
        self.minMaxTempLabel.setText(QCoreApplication.translate("weatherWindow", u"H: 32C L:26C", None))
        self.humidityLabel.setText(QCoreApplication.translate("weatherWindow", u"Hum: 62%", None))
        self.windSpeedLabel.setText(QCoreApplication.translate("weatherWindow", u"NW 12 knts", None))
        self.weatherIcon.setText("")
        self.forecastDateLabel_1.setText(QCoreApplication.translate("weatherWindow", u"09/11", None))
        self.forecastWeatherIcon_1.setText("")
        self.forecastTempLabel_1.setText(QCoreApplication.translate("weatherWindow", u"28C", None))
        self.forecastPerceivedLabel_1.setText(QCoreApplication.translate("weatherWindow", u"Mostly Cloudy", None))
        self.forecastHighLowTempLabel_1.setText(QCoreApplication.translate("weatherWindow", u"H: 32C L:26C", None))
        self.forecastDateLabel_2.setText(QCoreApplication.translate("weatherWindow", u"10/11", None))
        self.forecastWeatherIcon_2.setText("")
        self.forecastTempLabel_2.setText(QCoreApplication.translate("weatherWindow", u"28C", None))
        self.forecastPerceivedLabel_2.setText(QCoreApplication.translate("weatherWindow", u"Mostly Cloudy", None))
        self.forecastHighLowTempLabel_2.setText(QCoreApplication.translate("weatherWindow", u"H: 32C L:26C", None))
        self.forecastDateLabel_3.setText(QCoreApplication.translate("weatherWindow", u"11/11", None))
        self.forecastWeatherIcon_3.setText("")
        self.forecastTempLabel_3.setText(QCoreApplication.translate("weatherWindow", u"28C", None))
        self.forecastPerceivedLabel_3.setText(QCoreApplication.translate("weatherWindow", u"Mostly Cloudy", None))
        self.forecastHighLowTempLabel_3.setText(QCoreApplication.translate("weatherWindow", u"H: 32C L:26C", None))
        self.forecastDateLabel_4.setText(QCoreApplication.translate("weatherWindow", u"12/11", None))
        self.forecastWeatherIcon_4.setText("")
        self.forecastTempLabel_4.setText(QCoreApplication.translate("weatherWindow", u"28C", None))
        self.forecastPerceivedLabel_4.setText(QCoreApplication.translate("weatherWindow", u"Mostly Cloudy", None))
        self.forecastHighLowTempLabel_4.setText(QCoreApplication.translate("weatherWindow", u"H: 32C L:26C", None))
        self.forecastDateLabel_5.setText(QCoreApplication.translate("weatherWindow", u"13/11", None))
        self.forecastWeatherIcon_5.setText("")
        self.forecastTempLabel_5.setText(QCoreApplication.translate("weatherWindow", u"28C", None))
        self.forecastPerceivedLabel_5.setText(QCoreApplication.translate("weatherWindow", u"Mostly Cloudy", None))
        self.forecastHighLowTempLabel_5.setText(QCoreApplication.translate("weatherWindow", u"H: 32C L:26C", None))
        self.assistantButton.setText(QCoreApplication.translate("weatherWindow", u"Assistant", None))
        self.creditLabel.setText(QCoreApplication.translate("weatherWindow", u"Data provided by ", None))
        self.openWeatherIcon.setText("")
    # retranslateUi

