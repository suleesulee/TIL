//
//  ViewController.swift
//  Tab
//
//  Created by Seonguk Lee on 2021/02/09.
//

import UIKit

class ViewController: UIViewController {

    override func viewDidLoad() {
        super.viewDidLoad()
        // Do any additional setup after loading the view.
    }

    @IBAction func brnMoveImageView(_ sender: UIButton) {
        tabBarController?.selectedIndex = 1
    }
    
    @IBAction func btnDatePickerView(_ sender: UIButton) {
        tabBarController?.selectedIndex = 2
    }
}

