//
//  ViewController.swift
//  DatePicker
//
//  Created by Seonguk Lee on 2021/02/04.
//

import UIKit

class ViewController: UIViewController {
    let timeSelector: Selector = #selector(ViewController.updateTime)
    let interval = 1.0
    var count = 0

    @IBOutlet var lblCurrentTime: UILabel!
    @IBOutlet var lblPikerTime: UILabel!
    
    override func viewDidLoad() {
        super.viewDidLoad()
        // Do any additional setup after loading the view.
        
        Timer.scheduledTimer(timeInterval: interval, target: self, selector: timeSelector, userInfo: nil, repeats: true)
    }

    @IBAction func changerDatePicker(_ sender: UIDatePicker) {
        let datePickerview = sender
        
        let fomatter = DateFormatter()
        fomatter.dateFormat = "yyyy-MM-dd HH:mm EEE"
        lblPikerTime.text =
            "선택시간: " + fomatter.string(from: datePickerview.date)
    }
    
    @objc func updateTime() {
        //lblCurrentTime.text = String(count)
        //count += 1
        
        let date = NSDate()
        
        let formatter = DateFormatter()
        formatter.dateFormat = "yyyy-MM-dd HH:mm:ss EEE"
        lblCurrentTime.text = formatter.string(from: date as Date)
    }
}

