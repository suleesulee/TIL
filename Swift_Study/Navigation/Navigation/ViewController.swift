//
//  ViewController.swift
//  Navigation
//
//  Created by Seonguk Lee on 2021/02/10.
//

import UIKit

class ViewController: UIViewController, EditDelegate {
    let img1 = UIImage(named: "lamp1.png")
    let img2 = UIImage(named: "lamp2.jpg")
    
    var isOn = true
    var isZoom = false
    var orgZoom = false
    
    @IBOutlet var txtMessage: UITextField!
    @IBOutlet var imgView: UIImageView!
    
    override func viewDidLoad() {
        super.viewDidLoad()
        // Do any additional setup after loading the view.
        imgView.image = img1
    }
    
    override func prepare(for segue: UIStoryboardSegue, sender: Any?){
        let editViewController = segue.destination as! EditViewController
        if segue.identifier == "editButton"{
            editViewController.textWayValue = "segue : use button"
        } else if segue.identifier == "editBarButton" {
            editViewController.textWayValue = "segue : use Bar button"
        }
        editViewController.textMessage = txtMessage.text!
        editViewController.isOn = isOn
        editViewController.isZoom = orgZoom
        editViewController.delegate = self
    }
    
    func didMessageEditDone(_ controller: EditViewController, message: String) {
        txtMessage.text = message
    }
    
    func didImageOnOffDone(_ controller: EditViewController, isOn: Bool) {
        if isOn{
            imgView.image = img1
            self.isOn = true
        } else {
            imgView.image = img2
            self.isOn = false
        }
    }
    
    func didImageZoomDone(_ controller: EditViewController, isZoom: Bool) {
        let scale:CGFloat = 2.0
        var nWidth:CGFloat, nHeight:CGFloat
        
        if isZoom {
            if orgZoom{
                /* exception */
            } else {
                self.isZoom = false
                self.orgZoom = true
                nWidth = imgView.frame.width * scale
                nHeight = imgView.frame.height * scale
                imgView.frame.size = CGSize(width: nWidth, height: nHeight)
            }
        } else {
            if orgZoom {
                self.isZoom = true
                self.orgZoom = false
                nWidth = imgView.frame.width / scale
                nHeight = imgView.frame.height / scale
                imgView.frame.size = CGSize(width: nWidth, height: nHeight)
            } else {
                /* exception */
            }
        }
    }
}

